class Employee:
    ''' Employee Class  created by Narasimha '''
    
    def get_details(self):
        print("Employee Details") 


e1=Employee()
e2=Employee()
e3=Employee()
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)
print(Employee.__dict__)