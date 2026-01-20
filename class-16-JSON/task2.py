#Task 2: read emp.json file write data into user.json file
import json

fp1=open('emp.json','r')
fp2=open('user.json','w')  #NEW FILE WILL CREATE
employees=json.load(fp1)
json.dump(employees,fp2)
print("New file created successfully")

fp1.close()
fp2.close()