# from neo_api_client import NeoAPI
import io
import neo_api_client
import threading


def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)


# access_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJGaW50ZWNoMDA2IiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiJsUkpfdFpmc251Sl9BbEpROWZHOTlkNFB0VjBhIiwibmJmIjoxNjc4OTU5NTAyLCJhenAiOiJsUkpfdFpmc251Sl9BbEpROWZHOTlkNFB0VjBhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ua290YWtzZWN1cml0aWVzLm9ubGluZTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjE2Nzg5NjMxMDIsImlhdCI6MTY3ODk1OTUwMiwianRpIjoiZmNmODI4NzEtMWJjYy00YjM4LWJmZWQtZWU5ODdlZDMwNjZlIn0.bDTzcKdrYwA5hlPVD6R3eOISrdcKyVYPbTH14pULe1fBQy4QRiTQNlu060eGpuEEyvKPBUadzCEm6peY0yvHaaWV0tjSegi5rO-fC45ZsAdZpIPk-_aWHuv6se-u78DGuuiJEfXmU_nWC8d7oWwaONxNJF6NMP-PMKajratHvRk_mEJn2YEATXJIkgSCs-bpvW1z7EIouoDJhkCIYYCq4CVqR4r_BebQhT2HrjxAS68SxTD3rkORxO1rGeiqz5V7tnr3eQPrQcp1GBFKgwDcve5pLWN6GWsEEy9ZemIZQMdfGHTD_IPhNlLQyhMDGb2x1ML0nbxgHHlT9Wudj9LTVA"
# access_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT05fVVNFUiIsImF1ZCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJuYmYiOjE2Nzk2NTk2NDksImF6cCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJzY29wZSI6ImRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbmFwaS5rb3Rha3NlY3VyaXRpZXMuY29tOjQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6OTIyMzM3MjAzNjg1NDc3NSwiaWF0IjoxNjc5NjU5NjQ5LCJqdGkiOiI1YmE5YjFmNy0xOTY5LTRkNTUtOTdlYS04MTg4MDI0NWQ2NDgifQ.CEEK5Yqmrj8JKVFCb1D3q9fKjcJCGoIn9ZZxvjfbkdmK0Zs3ez1q2wCjh91E74UUhH7kEuYG6ioXrGR5WhfV-ens9R_U7fup8UOCibOp6FeluPNbJ77cctDxpY6WpyHfdz2LdK_eCBLhWIibq4z7Dr_qINZjwnZ9lkcWqtaX4OBO_RjhT8QH10wPwVLwy7eOMpSuhNVIJRHm6ZTQCkfemauXNmqB_LTtFxrvF4E7W7Z_gM-IH_1OSCR_nJY-mBuvv4HLHzzqFOBjCGsSrmC0lo9B7bOWkoeHerZ7txWuz2J3hdALZ-6Q7IZ2OCDFB1ucsYUl_j7tgMAQW7FUtRXZTQ "
# client = neo_api_client.NeoAPI(consumer_key="lRJ_tZfsnuJ_AlJQ9fG99d4PtV0a",
#                                consumer_secret="x6gk6ijpaOV7eKHojBmbFdVj92Qa", environment='uat', on_message=on_message,
#                                on_error=on_error)
client = neo_api_client.NeoAPI(consumer_key="f1X7OfHF2zLjMtSTT7C1PnLWDd0a",
                               consumer_secret="p3JilRTebrOUNBCfO8yQ_AhuKv0a", environment='prod',
                               on_message=on_message,
                               on_error=on_error)
# client.login(mobilenumber="+919999999908", password="P@ssword1234")
# client = neo_api_client.NeoAPI(access_token='',
#                                environment='prod', on_message=on_message,
#                                on_error=on_error)
client.login(mobilenumber="+918793189752", password="login@123")
a = client.session_2fa("123456")
print(a)
# print(client.search_scrip(exchange_segment="nse_fo", symbol="ICICI", expiry="", option_type="CE",strike_price=">505"))
print(client.search_scrip(exchange_segment="nse_fo", symbol="BANKNIFTY", expiry="", option_type="CE",strike_price="45000"))
# client.subscribe_to_orderfeed()
# print(type(a))
# s = client.scrip_master()
# print(s)
# s = client.limits(segment="CASH",exchange="ALL",product="CNC")
# print(s)
# s = client.scrip_master()
# print(s)
# client = neo_api_client.NeoAPI(access_token="eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiJmMVg3T2ZIRjJ6TGpNdFNUVDdDMVBuTFdEZDBhIiwibmJmIjoxNjgxOTc3MjIyLCJhenAiOiJmMVg3T2ZIRjJ6TGpNdFNUVDdDMVBuTFdEZDBhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL25hcGkua290YWtzZWN1cml0aWVzLmNvbTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjkyMjMzNzIwMzY4NTQ3NzUsImlhdCI6MTY4MTk3NzIyMiwianRpIjoiNTFlZmVlNmMtNTUxMS00ZWZmLWFkYmEtODZlNDk3MThhM2ZhIn0.aUZRtLo75BThlI3zP1El_0k5-U_dB36yaN_V_z72uTMMyLXeJt3MMDH7fN4c59kBwoPi6RwVk34Aa8jRY-qa1EmhVp9JKv78ImD1399uD2vWdKln85pa4Xenq7rYrlLv2T9x4KFPbZeg2XhO_sY1AkyKHy0oYpyTU6SDriG8p5geSwpXTSTTWe5ao9D8Sb6hKlDci5x2sB-iI2ktUQy9HBHAxHm44zDzZKRuqFqHazLcIgAL2HFERoV88h9HfTJqYPiG_rHaRuuJp35IaH773bWgacikVFZmPChH5Am98bWJsXfCj5YSIcflh9Dc9AKWpZEaIRm7x6lH_08ezqVi2w",environment="prod", on_message=on_message)
# a = client.search_scrip(exchange_segment="nse_fo", symbol="BANKNIFTY",  option_type="CE", expiry="18May2023",
#                         strike_price="45000")
# print(a)
# client.search_scrip(exchange_segment = "abcd")
# client.scrip_master(exchange_segment="233")
# client.search_scrip(exchange_segment='nse_cm', symbol = "YES")
# client.search_scrip(symbol="EURINR", exchange_segment="cde_fo", expiry="26May2023", option_type="PE",
#                     strike_price="855000000")

# a = client.scrip_master(exchange_segment="233")
# print(a)
# client.help("place_order")
# from neo_api_client import help
# client.help()
# client.help("order_report")
# client.help("quotes")
# client.help("holdings")
#
# instrument_tokens = [
#     {"instrument_token": "6530", "exchange_segment": "nse_cm"},
#     {"instrument_token": "6531", "exchange_segment": "nse_cm"},
#     {"instrument_token": "6532", "exchange_segment": "nse_cm"}
# ]
# client.subscribe(instrument_tokens=instrument_tokens)
# t1 = threading.Thread(target=client.subscribe(instrument_tokens=instrument_tokens))
# t1.start()
# inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"},
#                {"instrument_token": "1594", "exchange_segment": "nse_cm"},
#                {"instrument_token": "11915", "exchange_segment": "nse_cm"},
#                {"instrument_token": "13245", "exchange_segment": "nse_cm"}]
# client.un_subscribe(instrument_tokens=inst_tokens)
# t2 = threading.Thread(target=client.subscribe(instrument_tokens=inst_tokens))
# t2.start()
#
# in_tokens = [{"instrument_token": "6551", "exchange_segment": "nse_cm"},
#     {"instrument_token": "6553", "exchange_segment": "nse_cm"},
#     {"instrument_token": "6555", "exchange_segment": "nse_cm"}]
# t3 = threading.Thread(target=client.subscribe(instrument_tokens=in_tokens))
# t3.start()
# Start threads

# Wait for all threads to complete
# t1.join()
# t2.join()
# t3.join()
# print("instrument_tokens")
# print("Subscription is going to start ")

# a = client.quotes(instrument_tokens=inst_tokens, quote_type="scrip_details", isIndex=False)
# print(a)
# markets_depth
# ohlc
# ltp
# 52w
# circuit_limits
# scrip_details
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future1 = executor.submit(client.subscribe(instrument_tokens=instrument_tokens))
#     future2 = executor.submit(client.un_subscribe(instrument_tokens))
#
#     # Wait for both futures to complete
#     concurrent.futures.wait([future1, future2])

# client.un_subscribe(instrument_tokens)
# import multiprocessing
#
# proc1 = multiprocessing.Process(target=client.subscribe(instrument_tokens=instrument_tokens))
# inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"}]
# client.subscribe(instrument_tokens=instrument_tokens)
# inst_token = [{"instrument_token": "6542", "exchange_segment": "nse_fo"}]
# client.un_subscribe(inst_token)
#
# proc2 = multiprocessing.Process(target=client.subscribe(instrument_tokens=inst_tokens))
#
# proc1.start()
#
# proc2.start()
#
# proc1.join()
# proc2.join()


import json
import websocket

# class HSIWebSocket:
#     def __init__(self, url):
#         self.hsiSocket = None
#         self.reqData = None
#         self.hsiWs = None
#         self.OPEN = 0
#         self.readyState = 0
#         self.url = url
#         self.start_hsi_server(self.url)
#
#     def start_hsi_server(self, url):
#         print("INTO Start server ", url)
#         self.hsiWs = websocket.WebSocketApp(url,
#                                             on_message=self.on_message,
#                                             on_error=self.on_error,
#                                             on_close=self.on_close)
#         self.hsiWs.on_open = self.on_open
#         if self.hsiWs:
#             print("INTO HS WS BLOB")
#             self.hsiWs.binary_type = "blob"
#         else:
#             print("WebSocket not initialized!")
#         self.hsiWs.run_forever()
#
#     def on_message(self, ws, message):
#         print("Received message:", message)
#
#     def on_error(self, ws, error):
#         print("Error:", error)
#
#     def on_close(self, ws):
#         print("Connection closed")
#         self.OPEN = 0
#         self.readyState = 0
#         self.hsiWs = None
#
# def on_open(self, ws):
#     print("Connection established", self.url)
#     self.OPEN = 1
#     self.readyState = 1
#     auth = a['data']['token']
#     # 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE2ODMzMTE0MDAsImp0aSI6ImRmYWFhYjgzLWQzOTItNDA4NC05NDI4LTFkZThkZjBlMzI3NyIsImlhdCI6MTY4MzI1MjYwOCwiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6IkFCQ1hZWjA4IiwidWNjIjoiQUJDWFlaMDgiLCJuYXAiOiJBQkNERTExMDhIIiwiZmV0Y2hjYWNoaW5ncnVsZSI6MCwiY2F0ZWdvcmlzYXRpb24iOiIifQ.CGMPSKU0yM4olv2AyODfQ9LLrcIKghTBDUvIttrCAR_XsN6e2ZMOOj0kKjxsQBvL3g1VGC80b4LzeUPXXQ40ZbXHhqyZVj2eCDHRe_dwxWDDJwF7CLZTjKcbJdnHpVrqEyEG2OOHbnwoN_Ab3O3QYF7PX7Yy90GQ98PaaUdMsVIwTdxZawBSp3-aR22IdH7ubG7216Obe5TvmWVDQ_-_6u1v0tVrn5Nj0H_OW5ZnvlQYe7pWKNHWkZFCaCyQ-4ABIcROFvmsWHvUSdcrmYC_CEf1T6quR2_WHHThWqjCt96lj1FpEH8VvZqfT7m7smPDPU35Zw62rxIXbT8MKioYDA'
#     sid = a['data']['sid']
#     # '26cf5e38-de9c-47cc-b84c-458b9218dbd1'
#     server = 'WEB'
#     json_d = {"type": "CONNECTION", "Authorization": auth, "Sid": sid, "source": server}
#     self.send(json_d)
#
#     def send(self, d):
#         print("INTO send Server ", d)
#         reqJson = d
#         # reqJson = json.loads(d)
#         req = None
#         if reqJson['type'] == 'CONNECTION':
#             print("INside IF COnnection ")
#             if 'Authorization' in reqJson and 'Sid' in reqJson and 'source' in reqJson:
#                 req = {
#                     'type': 'cn',
#                     'Authorization': reqJson['Authorization'],
#                     'Sid': reqJson['Sid'],
#                     'source': reqJson['source']
#                 }
#                 self.reqData = req
#             else:
#                 if 'x-access-token' in reqJson and 'src' in reqJson:
#                     req = {
#                         'type': 'cn',
#                         'x-access-token': reqJson['x-access-token'],
#                         'source': reqJson['source']
#                     }
#                     self.reqData = req
#                 else:
#                     print("Invalid connection mode !")
#         else:
#             print("INside ELSE ")
#             if reqJson['type'] == 'FORCE_CONNECTION':
#                 self.reqData = self.reqData['type'] = 'fcn'
#                 req = self.reqData
#             else:
#                 print("Invalid Request !")
#         if self.hsiWs and req:
#             print("REQ", req)
#             print("hsiWs", self.hsiWs)
#             self.hsiWs.send(json.dumps(req))
#         else:
#             print("Unable to send request! Reason: Connection faulty or request not valid!")
#
#     def close(self):
#         self.hsiWs.close()
#         self.OPEN = 0
#         self.readyState = 0
#         self.hsiWs = None
#
# if __name__ == "__main__":
#     url = "wss://lhsi.kotaksecurities.com/realtime?sId=" + str(a['data']['hsServerId'])
#     hsiSocket = connect_hsm()
#     # hsiSocket.close()

# from neo_api_client import ConnectHSM
#
# url = "wss://lhsi.kotaksecurities.com/realtime?sId="
# ConnectHSM().hsm_connection(url=url, token=a['data']['token'], sid=a['data']['sid'],
#                             server_id=a['data']['hsServerId'])
