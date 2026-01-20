'''
read emp.csv and write emp data 
into new  user.csv file and 
csv file headers:uid,uname,salary
'''
import csv 
fp1=open('emp.csv','r')
emp_data=list(csv.reader(fp1))[1:]
print(emp_data)

fp2=open('user.csv','w',newline="")
csv_writer=csv.writer(fp2)
csv_writer.writerow(['uid','uname','salary'])
csv_writer.writerows(emp_data)
print(csv_writer)