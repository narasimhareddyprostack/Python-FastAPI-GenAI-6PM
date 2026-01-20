def login_required(func):
    def inner(name,login_status):
        if login_status==False:
            print("Login is Required")
        else:
            return func(name,login_status)
        
    return inner

def homepage(name,login_status):
    print("Home Page") 


def productpage(name,login_status):
    print("Product Page") 

@login_required
def orders(name,login_status):
    print("Order Page") 

@login_required
def profile(name,login_status):
    print("Profile Page") 

homepage("Rahul",False)
productpage("Rahul",False)
orders("Rahul",False)
profile("Rahul",False)