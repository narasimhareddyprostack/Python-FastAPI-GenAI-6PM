import requests
products=requests.get('https://dummyjson.com/products').json()['products']
print(len(products))

