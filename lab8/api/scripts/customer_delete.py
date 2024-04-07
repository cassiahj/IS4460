import requests

id = 1 #the customer id

#define the API endpoint
api_url=f'http://localhost:8000/api/customers/{id}/'

#send a get request to retrieve the customer
response=requests.delete(api_url)

#check the response status code
if response.status_code==204:
    print("Customer deleted successfully.")
else:
    print("Error retrieving the customer.")