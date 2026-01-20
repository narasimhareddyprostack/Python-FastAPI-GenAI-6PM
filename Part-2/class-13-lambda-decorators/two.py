def user_tr():
    print("user tr function started")

    def login():
        print("Login Success") 

    def logout():
        pass 

    return login

inn=user_tr()
inn()  #we are invoking login() -inner fun from outside  