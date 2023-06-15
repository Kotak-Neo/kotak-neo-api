# neo_api_client.login

# ***2FA to complete the login***

# Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
# The allowed combinations are :
    1. userId and password
    OR
    2. mobileNumber and password (You have to pass the country code as well in
        mobileNumber)
    OR
    3. pan and password

client.login(mobilenumber="+919999999999", password="XXXX")
# This will even send an OTP to the mobile number

# Complete login and generate session token
client.session_2fa(OTP="")

        """
        Logs in to the system by generating a view token using the provided mobile number and password.
        Generates an OTP (One-Time Password) for the user's session.

        Parameters:
        password (str): The password of the user.
        mobilenumber (str, optional): The mobile number of the user. Defaults to None.
        userid (str, optional): The user ID of the user. Defaults to None.
        pan (str, optional): The PAN (Permanent Account Number) of the user. Defaults to None.
        Either of pan/mobilenumber/userid has to pass to login

        Returns:
            {'data': {'token': '','sid': '', 'rid': '', 'hsServerId': '',isUserPwdExpired': , 'caches': {
        'baskets': '', 'lastUpdatedTS': '', 'multiplewatchlists': '', 'techchartpreferences': ''}, 'ucc': '',
        'greetingName': '', 'isTrialAccount': , 'dataCenter': '', 'searchAPIKey': ''}}


        Updates:
        view_token: sets the view token obtained from the API response.
        sid: sets the sid obtained from the API response.

        Raises:
        ApiException: if the view token or OTP generation fails.
        """

# Once the 2FA process is complete, you can access other methods.

