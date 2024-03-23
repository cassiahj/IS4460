import requests

id = 1 #the order id

#define the API endpoint
api_url=f'http://localhost:8000/api/customers/{id}/'

#send a get request to retrieve the order
response=requests.get(api_url)

#check the response status code
if response.status_code==200:
    order_data=response.json()
    print(order_data)
else:
    print("Error retrieving the order.")