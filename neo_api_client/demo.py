# from neo_api_client import NeoAPI
import neo_api_client


def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)


# access_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJGaW50ZWNoMDA2IiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiJsUkpfdFpmc251Sl9BbEpROWZHOTlkNFB0VjBhIiwibmJmIjoxNjc4OTU5NTAyLCJhenAiOiJsUkpfdFpmc251Sl9BbEpROWZHOTlkNFB0VjBhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ua290YWtzZWN1cml0aWVzLm9ubGluZTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjE2Nzg5NjMxMDIsImlhdCI6MTY3ODk1OTUwMiwianRpIjoiZmNmODI4NzEtMWJjYy00YjM4LWJmZWQtZWU5ODdlZDMwNjZlIn0.bDTzcKdrYwA5hlPVD6R3eOISrdcKyVYPbTH14pULe1fBQy4QRiTQNlu060eGpuEEyvKPBUadzCEm6peY0yvHaaWV0tjSegi5rO-fC45ZsAdZpIPk-_aWHuv6se-u78DGuuiJEfXmU_nWC8d7oWwaONxNJF6NMP-PMKajratHvRk_mEJn2YEATXJIkgSCs-bpvW1z7EIouoDJhkCIYYCq4CVqR4r_BebQhT2HrjxAS68SxTD3rkORxO1rGeiqz5V7tnr3eQPrQcp1GBFKgwDcve5pLWN6GWsEEy9ZemIZQMdfGHTD_IPhNlLQyhMDGb2x1ML0nbxgHHlT9Wudj9LTVA"
# access_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT05fVVNFUiIsImF1ZCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJuYmYiOjE2Nzk2NTk2NDksImF6cCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJzY29wZSI6ImRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbmFwaS5rb3Rha3NlY3VyaXRpZXMuY29tOjQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6OTIyMzM3MjAzNjg1NDc3NSwiaWF0IjoxNjc5NjU5NjQ5LCJqdGkiOiI1YmE5YjFmNy0xOTY5LTRkNTUtOTdlYS04MTg4MDI0NWQ2NDgifQ.CEEK5Yqmrj8JKVFCb1D3q9fKjcJCGoIn9ZZxvjfbkdmK0Zs3ez1q2wCjh91E74UUhH7kEuYG6ioXrGR5WhfV-ens9R_U7fup8UOCibOp6FeluPNbJ77cctDxpY6WpyHfdz2LdK_eCBLhWIibq4z7Dr_qINZjwnZ9lkcWqtaX4OBO_RjhT8QH10wPwVLwy7eOMpSuhNVIJRHm6ZTQCkfemauXNmqB_LTtFxrvF4E7W7Z_gM-IH_1OSCR_nJY-mBuvv4HLHzzqFOBjCGsSrmC0lo9B7bOWkoeHerZ7txWuz2J3hdALZ-6Q7IZ2OCDFB1ucsYUl_j7tgMAQW7FUtRXZTQ "
client = neo_api_client.NeoAPI(consumer_key="lRJ_tZfsnuJ_AlJQ9fG99d4PtV0a",
                               consumer_secret="x6gk6ijpaOV7eKHojBmbFdVj92Qa", environment='uat', on_message=on_message,
                               on_error=on_error)
client.login(mobilenumber="+919999999908", password="P@ssword1234")
client.session_2fa(OTP=input("ENTER OTP:- "))

instrument_tokens = [
    {"instrument_token": "6530", "exchange_segment": "nse_cm"},
    {"instrument_token": "6531", "exchange_segment": "nse_cm"},
    {"instrument_token": "6532", "exchange_segment": "nse_cm"},
    {"instrument_token": "6533", "exchange_segment": "nse_cm"},
    {"instrument_token": "6542", "exchange_segment": "nse_cm"},
    {"instrument_token": "6543", "exchange_segment": "nse_cm"},
    {"instrument_token": "6545", "exchange_segment": "nse_cm"},
    {"instrument_token": "6551", "exchange_segment": "nse_cm"},
    {"instrument_token": "6553", "exchange_segment": "nse_cm"},
    {"instrument_token": "6555", "exchange_segment": "nse_cm"}
]
print("instrument_tokens")
print("Subscription is going to start ")

# client.quotes(instrument_tokens=instrument_tokens, callback=on_message, quote_type="scrip_details", isIndex=True)

# market_depth
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
# client.subscribe(instrument_tokens=instrument_tokens)
# import multiprocessing
#
# proc1 = multiprocessing.Process(target=client.subscribe(instrument_tokens=instrument_tokens))
# inst_tokens = [{"instrument_token": "-11536", "exchange_segment": "nse_cm"}]
client.subscribe(instrument_tokens=instrument_tokens)
#
# proc2 = multiprocessing.Process(target=client.subscribe(instrument_tokens=inst_tokens))
#
# proc1.start()
#
# proc2.start()
#
# proc1.join()
# proc2.join()

print("Both Processes Completed!")
