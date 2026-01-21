class Account:
    min_bal=500

    def open_acc(self):
        print("Account Opened Successfully")     
    def deposit_amount(self):
        print("Amount Deposited")
    def withdrawl(self):
        print("Amount withdrawl")
    def get_bal(self):
        return 100
    def get_st(self):
        print("Getting Statement")
    def close_acc(self):
        print("Account Closed")

a1=Account()


a1.open_acc()
a1.deposit_amount()
a1.withdrawl()
a1.get_st()
bal=a1.get_bal()
print("Account Balance:",bal)
a1.close_acc()
