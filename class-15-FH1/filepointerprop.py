fp=open('data.txt','r')

print("File Pointer properites")
print(fp.name)
print(fp.readable())
print(fp.writable())
print(fp.closed)
fp.close()
print("After closing/releasing resource",fp.closed)
