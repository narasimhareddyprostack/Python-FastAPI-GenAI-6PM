#Task 3: read emp.json and write all male emp into male.json file
import json 
fp1=open('emp.json','r')
employees=json.load(fp1)

male_employees=[]
for emp in employees:
    if emp['gender']=="Male":
        male_employees.append(emp)

print('No of male employees',len(male_employees))

fp2=open('male.json','w')
json.dump(male_employees,fp2)
print('New male.json file created successfully')


fp1.close()
fp2.close()