fp1=open("data.txt",'r')
fp2=open("bangalore.txt",'w')

data=fp1.read()
fp2.write(data)

print("Data Written Successfully")
fp1.close()
fp2.close()
