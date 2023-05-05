import io
import json
import os

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
                # print("***", data)
                # print("***exchange_segment", exchange_segment)
                exchange_segment_csv = [file for file in data["filesPaths"] if exchange_segment.lower() in file.lower()]
                # print(exchange_segment_csv)
                response = requests.get(exchange_segment_csv[0])
                csv_text = response.text
                df = pd.read_csv(io.StringIO(csv_text))
                df = df.rename(columns=lambda x: x.strip())
                if expiry and strike_price and not exchange_segment.endswith('fo'):
                    return {'error': [
                        {'code': '10300', 'message': "The Give Segment doesn't have Expire and Strike Price "}]}
                if exchange_segment.endswith('fo'):
                    df['pExpiryDate'] = pd.to_datetime(df['pExpiryDate'], unit='s')
                    df['pExpiryDate'] = df['pExpiryDate'] + pd.DateOffset(years=10)
                    df['pExpiryDate'] = df['pExpiryDate'].dt.strftime('%d%b%Y')

                if symbol != '':
                    mask = df["pSymbolName"].str.lower().str.strip().str.contains(symbol)
                    df = df[mask]
                    # print(df.head(5))
                if option_type:
                    option_type = str(option_type).lower()
                    option_type = option_type.split(",")
                    df["pOptionType"] = df["pOptionType"].str.lower()
                    mask = df["pOptionType"].isin(option_type)
                    df = df[mask]
                    # print(df.head(5))
                if expiry:
                    list_expiry = expiry.split('-')
                    if len(list_expiry) > 2:
                        error = {
                            'error': [
                                {'message': "Format of Expiry Date is not proper. Kindly pass DDMMYYYY(01MAY2023)"}]}
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
                    strike_price = str(strike_price) + str('00.0')
                    if strike_price < '0':
                        error = {
                            'error': [
                                {'message': "Strike Won't be less than 0. So Kindly pass the proper value"}]}
                        return error
                    df['dStrikePrice;'] = df['dStrikePrice;'].astype(str)
                    list_strike_price = strike_price.split('-')
                    if len(list_strike_price) == 2:
                        min_strike_price, max_strike_price = list_strike_price[0], list_strike_price[1]
                        if min_strike_price > max_strike_price:
                            error = {
                                'error': [
                                    {'code': '10300',
                                     'message': 'Strike Price will has min value in first place and '
                                                'max value in 2nd place'}]}
                            return error
                        else:
                            df = df[min_strike_price < df['dStrikePrice;'] <= max_strike_price]
                    elif len(list_strike_price) == 1:
                        df = df[df['dStrikePrice;'] == list_strike_price[0]]
                    else:
                        error = {
                            'error': [
                                {'code': '10300',
                                 'message': 'Strike Price will be in the format of min_value-max_value or'
                                            'only one value'}]}
                        return error

                # print("LENGTH", len(df))
                df = df.dropna(how='all')
                # print(df.head(10))
                if len(df) > 0:
                    df = df.to_json(orient='records')
                    df = json.loads(df)
                    # df = json.dumps(df)
                    return df
                else:
                    return {"message": "With the Given Search Info the data is empty! Try with other combinations"}
            else:
                return {"error": "Exchange segment not found"}

        except ApiException as ex:
            return {"error": ex}


