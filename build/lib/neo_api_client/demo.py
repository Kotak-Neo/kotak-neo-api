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
# client.login(mobilenumber="+919999999908", password="P@ssword1234")
# client.session_2fa(OTP=input("ENTER OTP:- "))
# s = client.scrip_master()
# print(s)
client = neo_api_client.NeoAPI(
    access_token="eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiJmMVg3T2ZIRjJ6TGpNdFNUVDdDMVBuTFdEZDBhIiwibmJmIjoxNjgxOTc3MjIyLCJhenAiOiJmMVg3T2ZIRjJ6TGpNdFNUVDdDMVBuTFdEZDBhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL25hcGkua290YWtzZWN1cml0aWVzLmNvbTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjkyMjMzNzIwMzY4NTQ3NzUsImlhdCI6MTY4MTk3NzIyMiwianRpIjoiNTFlZmVlNmMtNTUxMS00ZWZmLWFkYmEtODZlNDk3MThhM2ZhIn0.aUZRtLo75BThlI3zP1El_0k5-U_dB36yaN_V_z72uTMMyLXeJt3MMDH7fN4c59kBwoPi6RwVk34Aa8jRY-qa1EmhVp9JKv78ImD1399uD2vWdKln85pa4Xenq7rYrlLv2T9x4KFPbZeg2XhO_sY1AkyKHy0oYpyTU6SDriG8p5geSwpXTSTTWe5ao9D8Sb6hKlDci5x2sB-iI2ktUQy9HBHAxHm44zDzZKRuqFqHazLcIgAL2HFERoV88h9HfTJqYPiG_rHaRuuJp35IaH773bWgacikVFZmPChH5Am98bWJsXfCj5YSIcflh9Dc9AKWpZEaIRm7x6lH_08ezqVi2w",
    environment="prod", on_message=on_message)
# client.search_scrip(exchange_segment = "abcd")
# client.scrip_master(exchange_segment="233")
# client.search_scrip(exchange_segment='nse_cm', symbol = "YES")
a = client.search_scrip(symbol="EURINR", exchange_segment="cde_fo", expiry="26May2023", option_type="PE",
                    strike_price="855000000")
print(type(a))
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
inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"},
               {"instrument_token": "1594", "exchange_segment": "nse_cm"},
               {"instrument_token": "11915", "exchange_segment": "nse_cm"},
               {"instrument_token": "13245", "exchange_segment": "nse_cm"}]
# client.subscribe(instrument_tokens=inst_tokens)
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

# client.quotes(instrument_tokens=inst_tokens, callback=on_message, quote_type="scrip_details", isIndex=False)

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


# import os
# import re
#
#
# def help(section=None):
#     # Get the path to the README.md file
#     readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
#
#     # Read the contents of the README.md file
#     with open(readme_path, 'r') as f:
#         readme_contents = f.read()
#
#     # Define regular expressions to extract section information
#     login_regex = r'### Login\n(.*?)\n\n'
#     place_order_regex = r'### Place Order\n(.*?)\n\n'
#
#     # Extract the relevant section information
#     if section == 'login':
#         section_info = re.search(login_regex, readme_contents, re.DOTALL).group(1)
#     elif section == 'place_order':
#         section_info = re.search(place_order_regex, readme_contents, re.DOTALL).group(1)
#     else:
#         # No section specified, display entire README.md file
#         section_info = readme_contents
#
#     # Print the relevant section information
#     print(section_info)
#
#
# help()
