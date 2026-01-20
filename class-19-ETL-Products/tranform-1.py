#Extract
import requests
products=requests.get('https://dummyjson.com/products').json()['products']
print(len(products))
#Traform
#Traform - for json file(expected list with dict data)
products_json=[]
for product in products:
    products_json.append({'product_id':product['id'],
                          'name':product['title'],
                          'price':product['price'],
                          'category':product['category'],
                          'rating':product['rating']
                          })

    
print(products_json)