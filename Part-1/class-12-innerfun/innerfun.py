def outer():
    print("outer function started")


    def login():
        print("Login Success")

    def logout():
        print("Logout")

    
    return login    #return the inner fun ref
    #return [10,20]
    #return "Hello"
    #return 100

inner=outer()

print(type(inner))
inner()
inner()

    
