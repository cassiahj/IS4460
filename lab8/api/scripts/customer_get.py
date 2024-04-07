import requests

id = 1 #the customer id

#define the API endpoint
api_url='http://localhost:8000/api/customers/'

#send a get request to retrieve the customer
response=requests.get(api_url)

#check the response status code
if response.status_code==200:
    customer_data=response.json()
    print(customer_data)
else:
    print("Error retrieving the customer.")