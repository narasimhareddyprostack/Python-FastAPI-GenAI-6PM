try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print(a+b)                      
    print(a/b)
    fp=open("data.txt",'r')
    print(fp.name)

except ValueError as err:
    print("Unable to Convert")

except ZeroDivisionError as err:
    print("Can't Devide by Zero") 

except FileNotFoundError as err :
    print("File Not Exists")

finally:
    print('finally Block will execute always! irrespecitve of try -except')
