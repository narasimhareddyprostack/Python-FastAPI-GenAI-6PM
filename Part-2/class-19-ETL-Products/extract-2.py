import requests

product_resp=requests.get('https://dummyjson.com/products')

products=product_resp.json()['products']
print(len(products))

