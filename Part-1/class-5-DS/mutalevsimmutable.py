#Mutalbe object in python?
""" 
list
set
dict 
bytearray 
"""

enames=['RG','SG']
enames.append("PG")
print(enames)

unames={'RG','SG'}
unames.add('PG')
print(unames)

emp = { 'eid':101,
        'ename':'Rahul',
        'esal':45000   
     }
emp['email']='rahul@ibm.com'
print(emp)

print("**********")
ba=bytearray([10,20,30,255])
ba[0]=11

for element in ba:
    print(element)