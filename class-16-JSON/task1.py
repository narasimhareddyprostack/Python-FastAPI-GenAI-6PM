#Task 1: read emp.json file print all employee names?

import json

fp=open('emp.json','r')
employees=json.load(fp)

for emp in employees:
    #print(type(emp))
    print(emp['ename'])

fp.close()
