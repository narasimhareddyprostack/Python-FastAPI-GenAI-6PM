import json 

employees="""
            {"eid":101,"ename":"Rahul","avail":true}
"""
emp_dict=json.loads(employees)
print(emp_dict)

#output
{'eid': 101, 'ename': 'Rahul', 'avail': True}

