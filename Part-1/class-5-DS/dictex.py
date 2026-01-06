d1={}  #empty dict
print(d1)
print(type(d1))
#create -
emp = { 'eid':101,
        'ename':'Rahul',
        'esal':45000   
     }
#read 
print(emp)
#how to read dict values? using key
print(emp['eid'])   #101
print(emp['ename']) #Rahul
print(emp['esal'])  #45000
#print(emp['gender'])  #KeyError

#update 
emp['ename']="Rahul Gandhi"
print(emp)

#delete
del emp['esal']
print(emp)