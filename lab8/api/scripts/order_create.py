import requests
import json

#define the API endpoint
api_url='http://localhost:8000/api/orders/'

#order data as an array of json objects
order_data= {"customer":"1",
             "total_price":"45.45",
             "total_items":"12",
             "order_date":""
                }

#create customers using a single post request
response = requests.post(url =api_url,
                         data=json.dumps(order_data),
                         headers={'Content-Type':'application/json'})

#check the repsonse and status code
if response.status_code==201:
    print("Order created successfully.")
else:
    print("Error creating the order.")