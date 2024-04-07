import requests

id = 1 #the order id

#define the API endpoint
api_url=f'http://localhost:8000/api/customers/{id}/'

#send a get request to retrieve the customer
response=requests.delete(api_url)

#check the response status code
if response.status_code==204:
    print("Order deleted successfully.")
else:
    print("Error retrieving the Order.")