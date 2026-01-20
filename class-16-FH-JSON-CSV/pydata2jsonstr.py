import json 

emp={'eid': 101, 'ename': 'Rahul', 'avail': True,'loc':None}

emp_str=json.dumps(emp)

print(emp_str)
print(type(emp_str))

#{"eid": 101, "ename": "Rahul", "avail": true,"loc": null}
#<class 'str'>
