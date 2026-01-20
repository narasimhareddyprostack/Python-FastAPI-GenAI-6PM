try:
    raise ZeroDivisionError("Cant divide by zero")
    print(10/0)
    print("GM")
    
except ZeroDivisionError as err:
    print(err) 


finally:
    print("Execute Always")




