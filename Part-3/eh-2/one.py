
try:
    fp=open("data.txt",'r')
    data=fp.read()
    print(data) 

except FileNotFoundError as err:
    print(err)

finally:
    print("finally block will execute always")
    fp.close()

print(fp.closed)


print("Good Evening...") 