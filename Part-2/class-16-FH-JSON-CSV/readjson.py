#Write Python script to read emp.json and print all employee names
import json

fp=open('emp.json','r')

employees=json.load(fp)

for emp in employees:
    print(emp['ename'])

fp.close()