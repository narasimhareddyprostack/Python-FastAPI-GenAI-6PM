def rbi_rule(func):
    def inner():
        pass 

    return inner


class Account:
    min_bal=500    #static/class level variable

    def __init__(self):
        self.acc_id=101         #instance variable
        self.acc_name="Rahul"
        self.acc_bal=6000
        print("Constrcutor Special method")

    @rbi_rule
    def update_roi():
        pass

    def deposit_amount(self,amount):
        print("Amount Deposited")

    @classmethod
    def update_min_bal(cls,amount):
        print("class method")

    @staticmethod
    def calc_interest():
        rate=5             #local variable
        print("static method")