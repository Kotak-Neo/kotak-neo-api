import copy
import json
import threading
import time

import neo_api_client
from neo_api_client.settings import stock_key_mapping, MarketDepthResp, QuotesChannel, \
    ReqTypeValues, index_key_mapping
from neo_api_client.urls import ORDER_FEED_URL


# from neo_api_client.logger import logger


class NeoWebSocket:
    def __init__(self, sid, token, server_id):
        self.hsiWebsocket = None
        self.is_hsi_open = 0
        self.un_sub_token = False
        self.sid = sid
        self.access_token = token
        self.server_id = server_id
        self.is_hsw_open = 0
        self.quotes_arr = []
        self.sub_list = []
        self.un_sub_list = []
        self.un_sub_channel_token = {}
        # self.quotes_api_callback = None
        self.hsWebsocket = None
        self.channel_tokens = {}
        self.live_scrip_type = None
        self.on_message = None
        self.on_error = None
        self.on_close = None
        self.on_open = None
        self.quotes_index = None
        self.un_sub_list_count = 0
        self.un_sub_channel = None
        self.token_limit_reached = False
        self.hsw_thread = None
        self.hsi_thread = None

    def start_hsi_ping_thread(self):
        while self.hsiWebsocket and self.is_hsi_open:
            time.sleep(30)
            payload = {"type": "HB"}
            self.hsiWebsocket.send(json.dumps(payload))

    def start_hsm_ping_thread(self):
        while self.hsWebsocket and self.is_hsw_open:
            time.sleep(29)
            payload = {"type": "hb"}
            self.hsiWebsocket.send(json.dumps(payload))

    def start_websocket(self):
        self.hsWebsocket = neo_api_client.HSWebSocket()
        self.hsWebsocket.open_connection(neo_api_client.WEBSOCKET_URL, self.access_token, self.sid,
                                         self.on_hsm_open, self.on_hsm_message,
                                         self.on_hsm_error, self.on_hsm_close)

    def start_websocket_thread(self):
        self.hsw_thread = threading.Thread(target=self.start_websocket)
        self.hsw_thread.start()
        # threading.Thread(target=self.start_hsm_ping_thread()).start()

    def on_hsm_open(self):
        print("On Open Function in Neo Websocket")
        req_params = {"type": "cn", "Authorization": self.access_token, "Sid": self.sid}
        self.hsWebsocket.hs_send(json.dumps(req_params))
        if self.on_open:
            self.on_open()

    def on_hsi_open(self):
        # print("HSI on open called")

        # print("On Open Function in Neo Websocket")
        server = 'WEB'
        json_d = {"type": "CONNECTION", "Authorization": self.access_token,
                  "Sid": self.sid,
                  "source": server}
        json_d = json.dumps(json_d)
        self.hsiWebsocket.send(json_d)

        if self.on_open:
            self.on_open()

    def on_hsm_message(self, message):
        # print("on Message Func in NeoWebsocket", message)
        if message:
            if type(message) == str:
                req_type = json.loads(message)[0]["type"]
                if req_type == 'cn':
                    # print("INSIDE CONNECTION")
                    self.is_hsw_open = 1
                    if len(self.quotes_arr) >= 1:
                        self.call_quotes()
                    if len(self.sub_list) >= 1:
                        self.subscribe_scripts(self.channel_tokens)
                if req_type == "unsub":
                    if len(self.un_sub_channel_token) > 0 and self.un_sub_channel:
                        # remove from sub_list and sub_token
                        self.remove_items(self.un_sub_channel_token[self.un_sub_channel])
                        del self.un_sub_channel_token[self.un_sub_channel]
                    if len(self.un_sub_channel_token) == 0:
                        if self.token_limit_reached:
                            self.sub_list = []
                            self.channel_tokens = {}
                            self.un_sub_channel_token = {}
                    if self.on_message:
                        self.on_message("Un-Subscribed Successfully!")
            elif type(message) == list:
                    if len(self.quotes_arr) >= 1:
                        out_list, quote_type = self.quote_response_formatter(message)
                        message = self.response_format(out_list, quote_type=quote_type)
                        # self.quotes_api_callback(message)
                        if self.on_message:
                            self.on_message(message)
                        self.quotes_arr = []
                    if len(self.sub_list) >= 1:
                        if self.on_message:
                            self.on_message(message)
                    
                    # If there is no other tokens in quotes_arr and sub_list. disconnect the socket
                    # print("sublist size ",len(self.sub_list))
                    if(len(self.sub_list)<=0):
                        self.hsWebsocket.close()

    def on_hsi_message(self, message):
        print("HSI on message called")
        if message:
            if isinstance(message, str):
                req = json.loads(message)
                if req["type"] == 'cn':
                    self.is_hsi_open = 1
                    threading.Thread(target=self.start_hsi_ping_thread()).start()
        if self.on_message:
           self.on_message(message)

    def on_hsm_close(self):
        print("On Close Function is running!")
        if self.is_hsw_open == 1:
            self.is_hsw_open = 0
        if self.on_close:
            self.on_close()

    def on_hsi_close(self):
        # print("HSI on close called")

        # print("On Close Function is running!")
        if self.is_hsi_open == 1:
            self.is_hsi_open = 0
        if self.on_close:
            self.on_close()

    def on_hsm_error(self, error):
        if self.is_hsw_open == 1:
            self.is_hsw_open = 0
            # if self.quotes_arr:
            #     self.quotes_api_callback(error)
        if self.hsWebsocket:
            self.hsWebsocket.close()
        if self.on_error:
            self.on_error(error)
        else:
            print("Error Occurred in Websocket! Error Message ", error)

    def on_hsi_error(self, error):
        print("HSI on error called")

        if self.is_hsi_open == 1:
            self.is_hsi_open = 0

        if self.on_error:
            self.on_error(error)
        else:
            print("Error Occurred in Websocket! Error Message ", error)


    def remove_items(self, un_sub_json):
        for unsubscribe_token in un_sub_json:
            token_value = unsubscribe_token[list(unsubscribe_token.keys())[0]]['instrument_token']
            segment_value = unsubscribe_token[list(unsubscribe_token.keys())[0]]['exchange_segment']
            sub_type_value = unsubscribe_token[list(unsubscribe_token.keys())[0]]['subscription_type']

            self.sub_list = [token for token in self.sub_list if str(list(token.keys())[0]) != str(token_value)]
            for channel_token_list in self.channel_tokens.values():
                for channel_token_dict in channel_token_list:
                    for channel_token_key, channel_token_value in channel_token_dict.items():

                        if token_value == channel_token_value['instrument_token'] and segment_value == \
                                channel_token_value['exchange_segment'] and sub_type_value == \
                                channel_token_value['subscription_type']:
                            channel_token_list.remove(channel_token_dict)
                            break

        return

    def input_validation(self, instrument_tokens):
        valid_params = ["instrument_token", "exchange_segment"]
        ret_obj = True
        if len(instrument_tokens) > 0:
            for item in instrument_tokens:
                if ret_obj:
                    keys_lst = list(item.keys())
                    for key in valid_params:
                        if key in keys_lst:
                            pass
                        else:
                            ret_obj = False
                            break
                else:
                    break
        else:
            ret_obj = False
        return ret_obj

    def get_formatted_data(self, instrument_tokens):
        scrips = ""
        quote_type = ""
        for item in instrument_tokens:
            for k, v in item.items():
                if type(v) == dict and "exchange_segment" in v.keys() and "instrument_token" in v.keys():
                    if scrips != "":
                        scrips += '&'
                    scrips += v["exchange_segment"] + "|" + str(v["instrument_token"])
                if k == "quote_type":
                    quote_type = v
        return scrips, quote_type

    def format_tokens_live(self, instrument_tokens):
        scrips = ""
        if type(instrument_tokens) == dict and "exchange_segment" in instrument_tokens.keys() and \
                "instrument_token" in instrument_tokens.keys():
            if scrips != "":
                scrips += '&'
            scrips += instrument_tokens["exchange_segment"] + "|" + str(instrument_tokens["instrument_token"])
        return scrips

    def format_un_sub_list(self, instrument_tokens):
        scrips = ""
        for instrument_token in instrument_tokens:
            if type(instrument_token) == dict and "exchange_segment" in instrument_token.keys() and \
                    "instrument_token" in instrument_token.keys():
                if scrips != "":
                    scrips += '&'
                scrips += instrument_token["exchange_segment"] + "|" + str(instrument_token["instrument_token"])
        return scrips

    def call_quotes(self):
        scrips, quote_type = self.get_formatted_data(self.quotes_arr)
        scrip_type = ReqTypeValues.get("SNAP_MW")
        if self.quotes_index:
            scrip_type = ReqTypeValues.get("SNAP_IF")
        else:
            if quote_type:
                if quote_type.strip().lower() == 'market_depth':
                    scrip_type = ReqTypeValues.get("SNAP_DP")
        
        req_params = json.dumps({"type": scrip_type, "scrips": scrips, "channelnum": QuotesChannel})
        self.hsWebsocket.hs_send(req_params)

    def quote_type_validation(self, quote_type):
        Q_type = True
        if quote_type:
            if str(quote_type).strip().lower() not in ['market_depth', 'ohlc', 'ltp', '52w', 'circuit_limits',
                                                       'scrip_details']:
                Q_type = False
        return Q_type

    def get_quotes(self, instrument_tokens, quote_type=None, isIndex=None):
        if self.quote_type_validation(quote_type):
            self.quotes_index = isIndex
            # self.quotes_api_callback = callback
            if self.input_validation(instrument_tokens):
                for item in instrument_tokens:
                    key = item['instrument_token']
                    value = {'instrument_token': item['instrument_token'],
                             'exchange_segment': item['exchange_segment']}
                    if key not in [list(x.keys())[0] for x in self.quotes_arr]:
                        self.quotes_arr.append({key: value, "quote_type": quote_type})
                    else:
                        index = [list(x.keys())[0] for x in self.quotes_arr].index(key)
                        self.quotes_arr[index][key].update(value)

                if self.hsWebsocket and self.is_hsw_open == 1:
                    self.call_quotes()
                else:
                    self.start_websocket_thread()

            else:
                return Exception("Invalid Inputs")
        else:
            try:
                raise ValueError(json.dumps({"Error": "Quote Type which is given is not matching",
                                             "Expected Values for quote_type": ['market_depth', 'ohlc', 'ltp',
                                                                                '52w',
                                                                                'circuit_limits',
                                                                                'scrip_details']}))
            except ValueError as e:
                print(str(e))

    def subscribe_scripts(self, channel_tokens):
        # print("self.channel_tokens.items()", self.channel_tokens)
        for channel, token_list in channel_tokens.items():
            for tokens in token_list:
                tokens = list(tokens.values())
                scrips = self.format_tokens_live(tokens[0])
                req_params1 = json.dumps(
                    {"type": tokens[0]["subscription_type"], "scrips": scrips, "channelnum": channel})
                self.hsWebsocket.hs_send(req_params1)

    def prepare_un_sub(self):
        # print("IN Prepare UNSUB")
        for key, value in self.channel_tokens.items():
            # Loop through each item in the value list
            for item in value:
                # Extract the subscription_type from the item
                subscription_type = list(item.values())[0]["subscription_type"]
                subscription_type = subscription_type.replace('s', 'u')
                # Create a new key by appending the subscription_type to the original key
                new_key = f"{key}-{subscription_type}"
                # Create a list to store the items as the value
                new_value = [{list(item.values())[0]["instrument_token"]: list(item.values())[0]}]
                # Add the item to the new_value list
                # Add the new key-value pair to un_sub_channel_token
                if new_key in self.un_sub_channel_token:
                    self.un_sub_channel_token[new_key].extend(new_value)
                else:
                    self.un_sub_channel_token[new_key] = new_value

        # print("IN Prepare UNSUB")
        # un_sub = copy.deepcopy(self.channel_tokens)
        # for key, value in un_sub.items():
        #     for item in value:
        #         for sub_key, sub_value in item.items():
        #             sub_value['subscription_type'] = sub_value['subscription_type'].replace('s', 'u')
        #
        # un_sub_list = []
        # for channel, data in un_sub.items():
        #     for items in data:
        #         list(items.values())[0]["channelnum"] = channel
        #         un_sub_list.append(list(items.values())[0])
        #
        # for items in un_sub_list:
        #     key = str(items["channelnum"]) + '-' + items["subscription_type"]
        #     del items["channelnum"]
        #     value = {items["instrument_token"]: items}
        #     if key not in self.un_sub_channel_token:
        #         self.un_sub_channel_token[key] = []
        #     self.un_sub_channel_token[key].append(value)
        # return

    def get_live_feed(self, instrument_tokens, isIndex, isDepth):
        if len(self.sub_list) + len(instrument_tokens) > 3000:
            self.token_limit_reached = True
            self.prepare_un_sub()
            self.un_subscription()

        tmp_token_list = []
        subscription_type = ReqTypeValues.get("SCRIP_SUBS")
        if isIndex:
            subscription_type = ReqTypeValues.get("INDEX_SUBS")
        if isDepth:
            subscription_type = ReqTypeValues.get("DEPTH_SUBS")

        if self.input_validation(instrument_tokens):
            for item in instrument_tokens:
                key = item['instrument_token']
                value = {'instrument_token': item['instrument_token'],
                         'exchange_segment': item['exchange_segment'],
                         'subscription_type': subscription_type}
                if 'subscription_type' not in item:
                    item['subscription_type'] = subscription_type
                if key not in [list(x.keys())[0] for x in self.sub_list]:
                    self.sub_list.append({key: value})
                    tmp_token_list.append({key: value})
                else:
                    index = [list(x.keys())[0] for x in self.sub_list].index(key)
                    if self.sub_list[index][key]['exchange_segment'] != item['exchange_segment'] or \
                            self.sub_list[index][key]['subscription_type'] != item['subscription_type']:
                        self.sub_list.append({key: value})
                        tmp_token_list.append({key: value})
                    else:
                        self.sub_list[index][key].update(value)
            channel_tokens = self.channel_segregation(tmp_token_list)
            if self.hsWebsocket and self.is_hsw_open == 1:
                self.subscribe_scripts(channel_tokens)

            else:
                self.start_websocket_thread()

        else:
            if self.on_error:
                self.on_error(Exception("Invalid Inputs"))

    def append_ohlc_data(self, new_dict):
        new_dict["ohlc"] = {}
        if 'open' in new_dict.keys():
            new_dict["ohlc"]["open"] = new_dict['open']
            new_dict.pop('open')
        else:
            new_dict["ohlc"]["open"] = None
        if 'high' in new_dict.keys():
            new_dict["ohlc"]["high"] = new_dict['high']
            new_dict.pop('high')
        else:
            new_dict["ohlc"]["high"] = None
        if 'low' in new_dict.keys():
            new_dict["ohlc"]["low"] = new_dict['low']
            new_dict.pop('low')
        else:
            new_dict["ohlc"]["low"] = None
        if 'close' in new_dict.keys():
            new_dict["ohlc"]["close"] = new_dict['close']
            new_dict.pop('close')
        else:
            new_dict["ohlc"]["close"] = None

        return new_dict

    def quote_type_filter(self, new_dict, quote_type):
        if quote_type:
            resp_dict = {'instrument_token': new_dict['instrument_token'],
                         'trading_symbol': new_dict['trading_symbol'],
                         'exchange_segment': new_dict['exchange_segment']}
            if quote_type.strip().lower() == 'ohlc':
                resp_dict['ohlc'] = new_dict['ohlc']
                return resp_dict
            elif quote_type.strip().lower() == 'ltp':
                resp_dict['ltp'] = new_dict['last_traded_price']
                return resp_dict
            elif quote_type.strip().lower() == '52w':
                resp_dict['52week_high'] = new_dict['52week_high']
                resp_dict['52week_low'] = new_dict['52week_low']
                return resp_dict
            elif quote_type.strip().lower() == 'circuit_limits':
                resp_dict['upper_circuit_limit'] = new_dict['upper_circuit_limit']
                resp_dict['lower_circuit_limit'] = new_dict['lower_circuit_limit']
                return resp_dict
            elif quote_type.strip().lower() == 'scrip_details':
                if "open_interest" in new_dict:
                    resp_dict['open_interest'] = new_dict['open_interest']
                resp_dict['last_traded_time'] = new_dict['last_traded_time']
                resp_dict['ltp'] = new_dict['last_traded_price']
                resp_dict['last_traded_quantity'] = new_dict['last_traded_quantity']
                resp_dict['total_buy_quantity'] = new_dict['total_buy_quantity']
                resp_dict['total_sell_quantity'] = new_dict['total_sell_quantity']
                resp_dict['volume'] = new_dict['volume']
                resp_dict['average_price'] = new_dict['average_price']
                resp_dict['volume'] = new_dict['volume']
                resp_dict['change'] = new_dict['change']
                resp_dict['net_change_percentage'] = new_dict['net_change_percentage']
                return resp_dict
            else:
                return new_dict
        else:
            return new_dict

    def depth_resp_mapping(self, response_data):
        final_response = []
        for item in response_data:
            depth_resp = {
                'instrument_token': item['tk'],
                'trading_symbol': item['ts'],
                'exchange_segment': item['e'],
                'depth': {
                    'buy': [
                        {'price': item['bp'], 'quantity': item['bq'], 'orders': item['bno1']},
                        {'price': item['bp1'], 'quantity': item['bq1'], 'orders': item['bno2']},
                        {'price': item['bp2'], 'quantity': item['bq2'], 'orders': item['bno3']},
                        {'price': item['bp3'], 'quantity': item['bq3'], 'orders': item['bno4']},
                        {'price': item['bp4'], 'quantity': item['bq4'], 'orders': item['bno5']},
                    ],
                    'sell': [
                        {'price': item['sp'], 'quantity': item['bs'], 'orders': item['sno1']},
                        {'price': item['sp1'], 'quantity': item['bs1'], 'orders': item['sno2']},
                        {'price': item['sp2'], 'quantity': item['bs2'], 'orders': item['sno3']},
                        {'price': item['sp3'], 'quantity': item['bs3'], 'orders': item['sno4']},
                        {'price': item['sp4'], 'quantity': item['bs4'], 'orders': item['sno5']},
                    ]
                }
            }
            final_response.append(depth_resp)
        return final_response

    def quote_resp_mapper(self, response_data, quote_type=None):
        out_resp = []
        if len(response_data) >= 1:
            for item in response_data:
                if type(item) == dict:
                    new_dict = {stock_key_mapping.get(k, k): v for k, v in item.items()}
                    for key in list(new_dict.keys()):
                        if key not in list(stock_key_mapping.values()):
                            new_dict.pop(key)
                    new_dict = self.append_ohlc_data(new_dict)
                    if quote_type:
                        if quote_type.strip().lower() != 'market_depth':
                            out_resp.append(self.quote_type_filter(new_dict, quote_type))
                    else:
                        out_resp.append(new_dict)
                else:
                    out_resp = response_data
        return out_resp

    def quote_response_formatter(self, message):
        quote_type = ''
        out_list = []
        quotes_arr_list = list(set().union(*(d.keys() for d in self.quotes_arr)))
        if "quote_type" in quotes_arr_list:
            quotes_arr_list.remove("quote_type")
        for item in message:
            if 'tk' in item:
                if item['tk'] in quotes_arr_list:
                    out_list.append(item)
                    for i in range(len(self.quotes_arr)):
                        if self.quotes_arr[i].get(item['tk']):
                            quote_type = self.quotes_arr[i]["quote_type"]
                        if self.quotes_arr[i].get(item['tk']):
                            del self.quotes_arr[i]
                            break
        return out_list, quote_type

    def response_format(self, response_data, quote_type):
        out_resp = []
        if self.quotes_index:
            if len(response_data) >= 1:
                for item in response_data:
                    if type(item) == dict:
                        new_dict = {index_key_mapping.get(k, k): v for k, v in item.items()}
                        for key in list(new_dict.keys()):
                            if key not in list(index_key_mapping.values()):
                                new_dict.pop(key)
                        out_resp.append(new_dict)

        else:
            if quote_type:
                if quote_type.strip().lower() == 'market_depth':
                    out_resp = self.depth_resp_mapping(response_data)
                else:
                    out_resp = self.quote_resp_mapper(response_data, quote_type)
            else:
                out_resp = self.quote_resp_mapper(response_data, quote_type)
        return out_resp

    def channel_segregation(self, tmp_token_list):
        # print("****** tmp_token_list", tmp_token_list)
        out_channel_list = {}
        for channel_num in range(2, 17):
            # Check if there is an existing channel array for this channel number
            if channel_num not in self.channel_tokens:
                self.channel_tokens[channel_num] = []
            if channel_num not in out_channel_list:
                out_channel_list[channel_num] = []

            # Check if there is space to add all the input JSON objects to this channel
            if len(self.channel_tokens[channel_num]) + len(tmp_token_list) <= 200:
                # Add all the input JSON objects to this channel
                self.channel_tokens[channel_num].extend(tmp_token_list)
                if out_channel_list[channel_num]:
                    out_channel_list[channel_num].extend(tmp_token_list)
                else:
                    out_channel_list[channel_num] = tmp_token_list
                # Exit the loop since all objects have been added to a channel
                break

            # Otherwise, add as many input JSON objects as possible to this channel
            num_to_add = 200 - len(self.channel_tokens[channel_num])
            self.channel_tokens[channel_num].extend(tmp_token_list[:num_to_add])
            out_channel_list[channel_num].extend(tmp_token_list[:num_to_add])
            # Remove the added objects from the input array
            tmp_token_list = tmp_token_list[num_to_add:]

        return out_channel_list

    def un_subscription(self):
        for channels, token_list in self.un_sub_channel_token.items():
            tokens_list = [list(tokens.values())[0] for tokens in token_list]
            scrips = self.format_un_sub_list(tokens_list)
            self.un_sub_channel = channels
            channel, sub_type = channels.split('-')
            req_params1 = json.dumps(
                {"type": sub_type, "scrips": scrips, "channelnum": channel})
            self.hsWebsocket.hs_send(req_params1)

    def un_subscribe_list(self, instrument_tokens, isIndex=False, isDepth=False):
        # print("INTO UNSUBSCRIBE", instrument_tokens)
        un_subscription_type = ReqTypeValues.get("SCRIP_UNSUBS")
        subscription_type = ReqTypeValues.get("SCRIP_SUBS")
        if isIndex:
            un_subscription_type = ReqTypeValues.get("INDEX_UNSUBS")
            subscription_type = ReqTypeValues.get("INDEX_SUBS")
        if isDepth:
            un_subscription_type = ReqTypeValues.get("DEPTH_UNSUBS")
            subscription_type = ReqTypeValues.get("DEPTH_SUBS")

        if self.input_validation(instrument_tokens):
            extracted_tokens = [{'instrument_token': item[key]['instrument_token'],
                                 'exchange_segment': item[key]['exchange_segment'],
                                 'subscription_type': item[key]['subscription_type']}
                                for item in self.sub_list for key in item]

            for token in instrument_tokens:
                token["subscription_type"] = subscription_type
                if token in extracted_tokens:
                    for key, value in self.channel_tokens.items():
                        for obj in value:
                            if list(obj.values())[0] == token:
                                in_key = token['instrument_token']
                                value = {'instrument_token': token['instrument_token'],
                                         'exchange_segment': token['exchange_segment'],
                                         'subscription_type': subscription_type}
                                key = str(key) + '-' + un_subscription_type
                                if key not in self.un_sub_channel_token:
                                    self.un_sub_channel_token[key] = []
                                self.un_sub_channel_token[key].append({in_key: value})

                else:
                    print("The Given Token is not in Subscription list")
            if self.hsWebsocket and self.is_hsw_open == 1:
                self.un_subscription()

            else:
                print("Socket Connection has been closed, So! The scripts are already un-subscribed!")

            # else:
            #     self.un_sub_token = True
            #     self.hsWebsocket = neo_api_client.HSWebSocket()
            #     self.hsWebsocket.open_connection(neo_api_client.WEBSOCKET_URL, self.access_token, self.sid,
            #                                      self.on_open, self.on_message, self.on_error, self.on_close)

    def start_hsi_websocket(self):
        url = ORDER_FEED_URL.format(server_id=self.server_id)
        self.hsiWebsocket = neo_api_client.HSIWebSocket()
        self.hsiWebsocket.open_connection(url=url, onopen=self.on_hsi_open,
                                          onmessage=self.on_hsi_message,
                                          onclose=self.on_hsi_close,
                                          onerror=self.on_hsi_error)

    def start_hsi_websocket_thread(self):
        self.hsi_thread = threading.Thread(target=self.start_hsi_websocket)
        self.hsi_thread.start()

    def get_order_feed(self):
        if self.hsiWebsocket is None or self.is_hsi_open == 0:
            self.start_hsi_websocket_thread()
        else:
            print("you had already subscribed for order feed")

       
