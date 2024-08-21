import requests
import hashlib
import json

# FawryPay API Endpoint
URL = "https://atfawry.fawrystaging.com/ECommerceWeb/Fawry/payments/charge"

# Payment Data
merchantCode = 'merchantCode' # HIDDEN
merchantRefNum = '23124654641'
merchant_cust_prof_id = '777777'
payment_method = 'PayUsingCC'
amount = '580.55'
cardNumber = '4242424242424242'
cardExpiryYear = '21'
cardExpiryMonth = '05'
cvv = '123'
returnUrl = 'https://developer.fawrystaging.com'
merchant_sec_key =  'API_KEY'  # HIDDEN
#signature = hashlib.sha256(merchantCode + (merchantRefNum) + (merchant_cust_prof_id) + (payment_method) +
#                (amount) + (cardNumber) + (cardExpiryYear) + (cardExpiryMonth) + (cvv) + (merchant_sec_key)).hexdigest()
#card_info= (merchantCode + merchantRefNum + merchant_cust_prof_id + payment_method +
#                amount + cardNumber + cardExpiryYear + cardExpiryMonth + cvv + merchant_sec_key)
card_info = ""
card_info=card_info +  (merchantCode  + merchantRefNum + payment_method +
				amount + cardNumber + cardExpiryYear + cardExpiryMonth + cvv +returnUrl+ merchant_sec_key)
print (card_info.encode())
signature = hashlib.sha256(str(card_info).encode('utf-8')).hexdigest()
#signature =hashlib.sha256(card_info.encode()).hexdigest()

# defining a params dict for the parameters to be sent to the API
PaymentData = {
    "merchantCode": merchantCode,
    "merchantRefNum": merchantRefNum,
    "cardNumber": cardNumber,
    "cardExpiryYear": cardExpiryYear,
    "cardExpiryMonth": cardExpiryMonth,
    "cvv": cvv,
    "customerMobile": "01111111111",
    "customerEmail": "a@gmail.com",
    "amount": amount,
    "currencyCode": "EGP",
    "language": "en-gb",
    "returnUrl": returnUrl,
    "chargeItems": [
        {
            "itemId": "184",
            "price": 580.55,
            "quantity": 1
        }
    ],
    "enable3DS": True,
    "paymentMethod": "CARD",
    "signature": signature
}

# Printing the data to be sent
print(json.dumps(PaymentData, indent=4))

# Setting headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Sending the POST request
status_request = requests.post(URL, json=PaymentData, headers=headers)

# Printing the response
print('Sent')
print(status_request.status_code)
print(status_request.text)

# Extracting data in JSON fo
