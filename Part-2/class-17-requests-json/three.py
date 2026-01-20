'''
usage:fetch all Products
API URL:https://dummyjson.com/products
Method Type:GET
Required Fields:None
Access Type:Public

Note: consume Rest API and display product data
'''

import requests 
product_resp=requests.get('https://dummyjson.com/products')

product_data=product_resp.json()
print(type(product_data))

