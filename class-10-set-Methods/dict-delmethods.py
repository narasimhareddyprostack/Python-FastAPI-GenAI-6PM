emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45
}

emp.pop('ename')

#dict.pop(key)  #remove specified key and value from dict
#dict.popitem() #remove last /arbitory key:value pair from dict
emp.popitem()
print(emp)