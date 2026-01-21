class Account:
    min_bal=500

      
    def deposit_amount(self,amount):
        print("Amount:",amount,"Deposited")
    def witdrawl_amount(self,amount):
        print("Amount withdrawl",amount)
    
    
   
a1=Account()
print(a1.min_bal)
a1.deposit_amount(5000)
a1.witdrawl_amount(50)


