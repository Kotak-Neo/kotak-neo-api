import neo_api_client


def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)


client = neo_api_client.NeoAPI(consumer_key="f1X7OfHF2zLjMtSTT7C1PnLWDd0a",
                               consumer_secret="p3JilRTebrOUNBCfO8yQ_AhuKv0a", environment='prod',
                               on_message=on_message,
                               on_error=on_error)

client.login(mobilenumber="+918793189752", password="login@123")
client.session_2fa(OTP="123456")

instrument_tokens = [{"instrument_token": "245896", "exchange_segment": "mcx_fo"}]
client.subscribe(instrument_tokens=instrument_tokens)