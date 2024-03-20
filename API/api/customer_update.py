import requests
import json

id = 1 #the customer id

#define the API endpoint
api_url=f'http://localhost:8000/api/customers/{id}/'

#customer data as an array of json objects
customer_data= {"name":"Customer YYYY",
                "email":"customerY@example.com",
                "phone_number":"8012344444"
                }

#send a put request to updte the customer
response=requests.put(api_url, data=json.dumps(customer_data),
                      headers={'Content-Type':'application/json'})

#check the response status code
if response.status_code==200:
    print("Customer updated successfully.")
else:
    print("Error retrieving the customer.")