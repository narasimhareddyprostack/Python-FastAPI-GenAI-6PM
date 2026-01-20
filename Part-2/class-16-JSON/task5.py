#read emp.json file and write non-gender employees into new nongender.json file

import json 
fp1=open('emp.json','r')
employees=json.load(fp1)  #JSON document to a Python object.

def verify_gender(emp):
    return emp['gender']!='Male' and emp['gender']!='Female'

non_gender=list(filter(verify_gender,employees))

print("No of Non-Gender Employees",len(non_gender))

fp2=open('non-gender.json','w')
json.dump(non_gender,fp2)
print('New file created Successfully')

fp1.close()
fp2.close()