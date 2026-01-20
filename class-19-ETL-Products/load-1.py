#Extract
import requests
import json
import csv

products=requests.get('https://dummyjson.com/products').json()['products']
print(len(products))
#Traform
#Traform - for json file(expected list with dict data)
products_json=[]
products_csv=[]
for product in products:
    products_json.append({'product_id':product['id'],
                          'name':product['title'],
                          'price':product['price'],
                          'category':product['category'],
                          'rating':product['rating']
                          })
    products_csv.append((product['id'],
                         product['title'],
                         product['price'],
                         product['category'],
                         product['rating']
                         ))

    
fp1=open('products.json','w')
fp2=open('products.csv','w')

#load data into csv ad json files

fp1.close()
fp2.close()