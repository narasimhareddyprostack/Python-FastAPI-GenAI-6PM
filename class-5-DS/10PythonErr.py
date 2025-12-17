#IndexError
eids=[101,102,103,104]
#index 0   1   2  3

print(eids[0])  #101
print(eids[1])  #102
#print(eids[8])  #IndexError: index out of range


#TypeError
enames=("RG","SG","PG")
enames[0]="Rahul Gandhi"
print(enames)

#TypeError: 'tuple' object does not support item assignment