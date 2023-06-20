import io
import json

import requests
from neo_api_client import rest
from neo_api_client.exceptions import ApiException
import pandas as pd


class ScripSearch(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = rest.RESTClientObject(api_client.configuration)

    def scrip_search(self, symbol, exchange_segment, expiry, option_type, strike_price,
                     ignore_50multiple):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}

        URL = self.api_client.configuration.get_url_details("scrip_master")

        try:
            scrip_report = self.rest_client.request(
                url=URL, method='GET',
                headers=header_params
            )

            data = scrip_report.json()["data"]

            if exchange_segment is not None:
                exchange_segment_csv = [file for file in data["filesPaths"] if exchange_segment.lower() in file.lower()]
                response = requests.get(exchange_segment_csv[0])
                csv_text = response.text
                df = pd.read_csv(io.StringIO(csv_text))
                df = df.rename(columns=lambda x: x.strip())

                if expiry and strike_price and not exchange_segment.endswith('fo'):
                    return {'error': [
                        {'code': '10300', 'message': "The given segment doesn't have expire and strike price"}]}

                if exchange_segment.endswith('fo'):
                    df['pExpiryDate'] = pd.to_datetime(df['pExpiryDate'], unit='s')
                    df['pExpiryDate'] = df['pExpiryDate'] + pd.DateOffset(years=10)
                    df['pExpiryDate'] = df['pExpiryDate'].dt.strftime('%d%b%Y')

                if symbol != '':
                    mask = df["pSymbolName"].str.lower().str.strip().str.contains(symbol)
                    df = df[mask]

                if option_type:
                    option_type = str(option_type).lower()
                    option_type = option_type.split(",")
                    df["pOptionType"] = df["pOptionType"].str.lower()
                    mask = df["pOptionType"].isin(option_type)
                    df = df[mask]

                if expiry:
                    list_expiry = expiry.split('-')
                    if len(list_expiry) > 2:
                        error = {
                            'error': [
                                {'message': "Format of expiry date is not proper. Kindly pass DDMMYYYY(01MAY2023)"}]}
                        return error
                    elif len(list_expiry) == 2:
                        df['pExpiryDate'] = pd.to_datetime(df['pExpiryDate'], format='%d%b%Y')
                        df = df[(df['pExpiryDate'] >= pd.to_datetime(list_expiry[0])) & (
                                df['pExpiryDate'] <= pd.to_datetime(list_expiry[1]))]
                        df['pExpiryDate'] = df['pExpiryDate'].dt.strftime('%d%b%Y')
                    else:
                        df['pExpiryDate'] = pd.to_datetime(df['pExpiryDate'], format='%d%b%Y')
                        df = df[df['pExpiryDate'] == pd.to_datetime(list_expiry[0])]
                        df['pExpiryDate'] = df['pExpiryDate'].dt.strftime('%d%b%Y')

                if strike_price:
                    df['dStrikePrice;'] = df['dStrikePrice;'].astype(float)
                    if '>' in strike_price:
                        strike_price = strike_price.split('>')
                        min_strike_price = float(strike_price[1])
                        df = df[df['dStrikePrice;'] >= min_strike_price]
                    elif '<' in strike_price:
                        strike_price = strike_price.split('<')
                        max_strike_price = float(str(strike_price[1]) + str('00.0'))
                        df = df[df['dStrikePrice;'] <= max_strike_price]
                    else:
                        list_strike_price = strike_price.split('-')
                        if len(list_strike_price) == 2:
                            min_strike_price, max_strike_price = float(list_strike_price[0]) * 100, float(
                                list_strike_price[1]) * 100
                            if min_strike_price > max_strike_price:
                                error = {
                                    'error': [
                                        {'code': '10300', 'message': 'The minimum strike price should be less than '
                                                                     'the maximum strike price.'}]
                                }
                                return error
                            else:
                                df = df[(df['dStrikePrice;'] >= min_strike_price) & (
                                        df['dStrikePrice;'] <= max_strike_price)]
                        elif len(list_strike_price) == 1:
                            if (float(list_strike_price[0]) * 100) <= 0:
                                error = {
                                    'error': [
                                        {
                                            'message': "Strike price cannot be less than 0. Please provide a valid "
                                                       "value."}]
                                }
                                return error
                            else:
                                df = df[df['dStrikePrice;'] == float(list_strike_price[0]) * 100]
                        else:
                            error = {
                                'error': [
                                    {'code': '10300', 'message': 'Strike price should be in the format of '
                                                                 'min_value-max_value or only one value.'}]
                            }
                            return error

                    df = df.dropna(how='all')
                    if len(df) > 0:
                        df = df.to_json(orient='records')
                        df = json.loads(df)
                        return df
                    else:
                        return {"message": "No data found with the given search information."
                                           "Please try with other combinations."}
                else:
                    return {"error": "Exchange segment not found."}

        except ApiException as ex:
            return {"error": ex}
