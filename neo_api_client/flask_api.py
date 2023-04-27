from flask import Flask, request, render_template, jsonify
import neo_api_client

app = Flask(__name__)


def on_message(message):
    # print(["RES :"], message)
    print("INTO ON Message Function ")
    return jsonify(message)
    # return render_template('index.html', callback=jsonify({"callback": message}))


# FROM JS it will hit python API then the rendering should happen from JS
# Logger with threading ----
# Create Python Server! Implement Websocket from Localhost from JS to connect
@app.route('/demo', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE2Nzk2ODI2MDAsImp0aSI6Ijk1ODlmOWE4LTlkZTYtNGNmOC04ZDE5LWIwMTI5MTA5OTA5ZSIsImlhdCI6MTY3OTY1OTY2NSwiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6ImZmZmMyMDgyLTdiMTktNGFkOC1iY2Q5LTdiNWM0NWZhMzZhZiIsInVjYyI6IllSSUowIiwicGFuIjoiSExQUEs4OTM2TCIsImZldGNoY2FjaGluZ3J1bGUiOjAsImNhdGVnb3Jpc2F0aW9uIjoiIn0.Iu9bfqXctlEL-2hDtvi2O14vwd7ZQSTQtH6_QfgbvUFlrJjucLXvwCrI2wZhkf2tp8KX3VZgUjUAh0I2GpjKqdrIOyKl_JmYmxHf1LyEFwmn3Pf9kcXIHbmLgcXcyFhtvKDNXsA5DfRZAfDwUCsFzJ62-98WkM3X2W2H7YZ9Uf9cM4INpVAqhB54b07znyRgv3CcWGdc6SVLLYQU9-JfFY5FqcK6L17ZvDePK95G8G2ZlTx-0kc9P6O7KvPPZBTN4dMwSumvsy3copPbAcmNVsKq-96SFZ5UxoUQspOc0yamZKZNV1LP-mB5LXSGczqs4ohifG4hWfaGEqqIg3XD5w"
        sid = "76c25769-5893-4a6b-897f-f4ef406d9455"
        server_id = "server2"
        access_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT05fVVNFUiIsImF1ZCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJuYmYiOjE2Nzk2NTk2NDksImF6cCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJzY29wZSI6ImRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbmFwaS5rb3Rha3NlY3VyaXRpZXMuY29tOjQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6OTIyMzM3MjAzNjg1NDc3NSwiaWF0IjoxNjc5NjU5NjQ5LCJqdGkiOiI1YmE5YjFmNy0xOTY5LTRkNTUtOTdlYS04MTg4MDI0NWQ2NDgifQ.CEEK5Yqmrj8JKVFCb1D3q9fKjcJCGoIn9ZZxvjfbkdmK0Zs3ez1q2wCjh91E74UUhH7kEuYG6ioXrGR5WhfV-ens9R_U7fup8UOCibOp6FeluPNbJ77cctDxpY6WpyHfdz2LdK_eCBLhWIibq4z7Dr_qINZjwnZ9lkcWqtaX4OBO_RjhT8QH10wPwVLwy7eOMpSuhNVIJRHm6ZTQCkfemauXNmqB_LTtFxrvF4E7W7Z_gM-IH_1OSCR_nJY-mBuvv4HLHzzqFOBjCGsSrmC0lo9B7bOWkoeHerZ7txWuz2J3hdALZ-6Q7IZ2OCDFB1ucsYUl_j7tgMAQW7FUtRXZTQ"

        input_text = request.form['input_text']

        client = neo_api_client.NeoAPI(access_token=access_token)
        qt = client.quotes(session_token=session_token, sid=sid, server_id=server_id,
                           instrument_tokens=input_text, callback=on_message, quote_type="scrip_details")

        return render_template('index.html', callback=qt)
    else:
        return render_template('index.html')


@app.route('/live_feed', methods=['POST', 'GET'])
def send_message():
    instrument_tokens = [{"instrument_token": "6530", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6531", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6532", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6533", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6542", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6543", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6545", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6551", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6553", "exchange_segment": "nse_cm"},
                         {"instrument_token": "6555", "exchange_segment": "nse_cm"}]

    # message = request.json['message']
    session_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE2Nzk2ODI2MDAsImp0aSI6Ijk1ODlmOWE4LTlkZTYtNGNmOC04ZDE5LWIwMTI5MTA5OTA5ZSIsImlhdCI6MTY3OTY1OTY2NSwiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6ImZmZmMyMDgyLTdiMTktNGFkOC1iY2Q5LTdiNWM0NWZhMzZhZiIsInVjYyI6IllSSUowIiwicGFuIjoiSExQUEs4OTM2TCIsImZldGNoY2FjaGluZ3J1bGUiOjAsImNhdGVnb3Jpc2F0aW9uIjoiIn0.Iu9bfqXctlEL-2hDtvi2O14vwd7ZQSTQtH6_QfgbvUFlrJjucLXvwCrI2wZhkf2tp8KX3VZgUjUAh0I2GpjKqdrIOyKl_JmYmxHf1LyEFwmn3Pf9kcXIHbmLgcXcyFhtvKDNXsA5DfRZAfDwUCsFzJ62-98WkM3X2W2H7YZ9Uf9cM4INpVAqhB54b07znyRgv3CcWGdc6SVLLYQU9-JfFY5FqcK6L17ZvDePK95G8G2ZlTx-0kc9P6O7KvPPZBTN4dMwSumvsy3copPbAcmNVsKq-96SFZ5UxoUQspOc0yamZKZNV1LP-mB5LXSGczqs4ohifG4hWfaGEqqIg3XD5w"
    sid = "76c25769-5893-4a6b-897f-f4ef406d9455"
    server_id = "server2"
    access_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT05fVVNFUiIsImF1ZCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJuYmYiOjE2Nzk2NTk2NDksImF6cCI6ImYxWDdPZkhGMnpMak10U1RUN0MxUG5MV0RkMGEiLCJzY29wZSI6ImRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbmFwaS5rb3Rha3NlY3VyaXRpZXMuY29tOjQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6OTIyMzM3MjAzNjg1NDc3NSwiaWF0IjoxNjc5NjU5NjQ5LCJqdGkiOiI1YmE5YjFmNy0xOTY5LTRkNTUtOTdlYS04MTg4MDI0NWQ2NDgifQ.CEEK5Yqmrj8JKVFCb1D3q9fKjcJCGoIn9ZZxvjfbkdmK0Zs3ez1q2wCjh91E74UUhH7kEuYG6ioXrGR5WhfV-ens9R_U7fup8UOCibOp6FeluPNbJ77cctDxpY6WpyHfdz2LdK_eCBLhWIibq4z7Dr_qINZjwnZ9lkcWqtaX4OBO_RjhT8QH10wPwVLwy7eOMpSuhNVIJRHm6ZTQCkfemauXNmqB_LTtFxrvF4E7W7Z_gM-IH_1OSCR_nJY-mBuvv4HLHzzqFOBjCGsSrmC0lo9B7bOWkoeHerZ7txWuz2J3hdALZ-6Q7IZ2OCDFB1ucsYUl_j7tgMAQW7FUtRXZTQ"

    client = neo_api_client.NeoAPI(access_token=access_token, on_message=on_message)
    print("client ", client)
    qt = client.subscribe(instrument_tokens=instrument_tokens)
    return render_template('index.html', callback=qt)
    # if request.method == 'GET':
    # return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
