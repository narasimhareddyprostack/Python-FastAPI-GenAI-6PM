'''
Write py script to read  - emp.csv file
and print all employee names
'''
import  csv 
fp=open('emp.csv','r')
emp_csv_data=list(csv.reader(fp))
print(emp_csv_data)

#list slicing
for emp in emp_csv_data[1:]:
    print(emp[1])
