def smart_division(func):
    print("Inside Decorator")
    def inner(a,b):
        if b==0:
            print("Cant Divibe Zero")
        else:
            return func(a,b)
        
    return inner 


@smart_division
def calc(a,b):
    return a/b 


print(calc(10,5))   #2.0
print(calc(10,0))   #10.0
