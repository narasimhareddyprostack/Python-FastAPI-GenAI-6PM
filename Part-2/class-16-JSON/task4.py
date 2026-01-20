#Task 3: read emp.json and write all male emp into male.json file
import json 
fp1=open('emp.json','r')
employees=json.load(fp1)

female_employees=list(filter(lambda emp:emp['gender']=="Female",employees))

print('No of female employees',len(female_employees))

fp2=open('female.json','w')

json.dump(female_employees,fp2)
print('New male.json file created successfully')


fp1.close()
fp2.close()