data=[10,20,30,40,255]
b=bytes(data)
ba=bytearray(data)

#b[0] = 11
ba[0]= 11
for value in ba:
    print(value)

'''
4/14 - Mutable object 
list,set,dict,bytearray
'''