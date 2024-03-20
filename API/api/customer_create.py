import requests
import json

#define the API endpoint
api_url='http://localhost:8000/api/customers/'

#customer data as an array of json objects
customer_data= {"name":"Customer X",
                "email":"customerX@example.com",
                "phone_number":"8012342345"
                }

#create customers using a single post request
response = requests.post(url =api_url,
                         data=json.dumps(customer_data),
                         headers={'Content-Type':'application/json'})

#check the repsonse and status code
if response.status_code==201:
    print("Customer created successfully.")
else:
    print("Error creating the customer.")