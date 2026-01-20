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
json.dump(products_json,fp1)
print("New Json file created and Data written successfully!")
csv_writer=csv.writer(fp2)
csv_writer.writerow(['product_id','name','price','category','rating'])
csv_writer.writerows(products_csv)
print("New CSV file createad successfully")

fp1.close()
fp2.close()