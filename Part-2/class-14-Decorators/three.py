def login_required(func):
    def inner(name,login_status):
        if login_status==False:
            print("Login is Required")
        else:
            return func(name,login_status)
        
    return inner

def homepage(name,login_status):
    print("Home Page") 



def orders(name,login_status):
    print("Order Page") 

homepage("Rahul",False)
orders("Rahul",False)
