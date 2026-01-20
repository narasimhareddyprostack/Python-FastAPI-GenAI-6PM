'''
usage:get all users
API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Required Fields:None
Access Type:Public
Note: invoke/consume restapi and display all user names
'''
import requests 
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')

users=user_resp.json()

for user in users:
    print(user['username'])

