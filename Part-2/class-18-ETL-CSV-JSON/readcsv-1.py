'''
Write py script to read  - emp.csv file
and print all employee names
'''
import  csv 
fp=open('emp.csv','r')
csv_reader=csv.reader(fp)
print(csv_reader)

for emp in csv_reader:
    print(emp[1])
