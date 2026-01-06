eids=[101,102,103,104]
print(101 in eids)   #True
print(101 not in eids)   #False

enames=("RG","SG","PG","Modi")
print("SG" in enames)  #True
print("alia Butt" in enames)  #False
sizes={'S','M','L','XL'}

print('XXL' in sizes)  #False

b=bytes([10,20,30,255])
ba=bytearray([10,20,30,255])
fz=frozenset({10,20,10,20})
numbers=range(100)

print( 10 in b)
print( 10 in ba)
print( 10 in fz)
print( 10 in numbers)


ename="Rahul"
print('R' in ename)  #True 
print('z' in ename)  #False 