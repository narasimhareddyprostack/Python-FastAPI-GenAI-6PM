def outer():
    print("outer function started")

    def inner():
        print("Inner Function")

    
    return inner    #return the inner fun ref
    #return [10,20]
    #return "Hello"
    #return 100

r1=outer()

print(type(r1))
r1()
r1()
r1()
    
