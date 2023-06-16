#  **place_new_order**

# The place_order function is used to submit a new order using the NEO API . 
# It takes several parameters to define the order details and performs validations before placing the order.
 

Place a New Order:

**Sample Request:**

        from neo_api_client import NeoAPI
        
        #First initialize session and generate session token

        client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment='')
        client.login(mobilenumber=" ", password=" ")
        client.session_2fa("")

        try:
            # Place a Order
            client.place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',
                    transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None)
        except Exception as e:
            print("Exception when calling OrderApi->place_order: %s\n" % e)


**Parameters**

**Name**                                **Values**                            **Description**

amo(optional)                           YES/NO - (Default Value - NO)
disclosed_quantity(optional)            String - (Default Value - 0)
exchange_segment                        nse_cm NSE 
                                        bse_cm BSE
                                        nse_fo NFO 
                                        bse_fo BFO 
                                        cde_fo CDS 
                                        bcs_fo BCD 
market_protection(optional)             String - (Default Value - 0)
product                                 NRML Normal
                                        CNC Cash and Carry 
                                        MIS MIS          
                                        INTRADAY INTRADAY
                                        CO Cover Order   
                                        BO Bracket Order 
pf(optional)                            Default Value - “N”
price                                   string
order_type                              L Limit 
                                        MKT Market    
                                        SL Stop loss limit 
                                        SL-M Stop loss  market
                                        SP Spread     
                                        2L Two Leg    
                                        3L Three Leg
quantity                                string
validity                                DAY, IOC
trigger_price(optional)                 String - (Default Value - 0)
trading_symbol                          string
transaction_type                        B(Buy), S(Sell)
tag(optional)                           string


**Return type:** Object

**Sample response:**               
               {
                'stat': 'Ok',
                'nOrdNo': '230120000017243',
                'stCode': 200
                }


