class Budget:
    def __init__(self, category, funds=0,):
        self.balance = funds
        self.category = category

    def depositFunds(self, funds):
        self.balance = funds
        return ("you have have deposited {0} to {1}".format(funds,self.category))

    def withdraw(self, amount):
        if (self.balance > amount):
              self.balance -= amount
              return ("you have withdrawn {0} from {1}".format(amount,self.category))
        else:
            return("insufficient balance")

    def computeBalance(self):
        return ("your {0} account balance is {1}".format(self.category,self.balance))

    def transferBalance(self, other):
           self.balance += other.balance
           response=("you have transferred a balance of {0} from {1} account to {2} account".format( other.balance, other.category,self.category))
           other.balance=0
           return response
       
           
food=Budget("food")
clothing=Budget("clothing", 2000)
print(food.depositFunds(1000))
print(clothing.computeBalance())
print(food.computeBalance())
print(food.transferBalance(clothing))
print(food.computeBalance())
print(clothing.computeBalance())
