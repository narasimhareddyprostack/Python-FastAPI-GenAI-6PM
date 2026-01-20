#Extract data from sourc
import csv 
fp1=open("emp.csv",'r')
emp_data=list(csv.reader(fp1))
#print(list(emp_data))

#transform
users=[]
for emp in emp_data:
    users.append([emp[0],emp[1],emp[2]])

print(users)


#load - write data into  new  csv file(csv).
fp2=open('user.csv','w')

csv_writer=csv.writer(fp2)

csv_writer.writerow(['eid','ename','esalary'])
csv_writer.writerows(users)

print(csv_writer)



