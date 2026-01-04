emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45
}
print(emp.values())
print(emp.keys())
print(emp.items())

for key in emp.keys():
    print(key)

for value in emp.values():
    print(value)

for key,value in emp.items():
    print(key,":",value)