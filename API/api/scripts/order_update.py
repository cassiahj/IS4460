import requests
import json

id = 1 #the customer id

#define the API endpoint
api_url=f'http://localhost:8000/api/orders/{id}/'

#order data as an array of json objects
order_data= {"customer":"1",
             "total_price":"122.34",
             "total_items":"8",
             "order_date":""
                }

#send a put request to update the order
response=requests.put(api_url, data=json.dumps(order_data),
                      headers={'Content-Type':'application/json'})

#check the response status code
if response.status_code==200:
    print("Order updated successfully.")
else:
    print("Error retrieving the order.")