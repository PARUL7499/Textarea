class bank :
    def getstatus(self):
        print(f"the bank name = {self.bankname}")
        print(f"the acc balance = {self.accbalance}")
        print("==================")

    def deposite(self,amount):
        self.accbalance = self.accbalance + amount
        print(f"the amount {amount} deposite successfully!")
        print (f"==============")

    def withdrawal(self,amount):
        if self.accbalance >  amount:
            self.accbalance = self.accbalance - amount
            print("withdrawal successfull")
        else:
            print("not enough money")
            print("===================")

b1 = bank() 
b1.bankname = "SBI"
b1.accbalance = 100000
b1.getstatus()           

b1.deposite(5000)
b1.getstatus()

b1.withdrawal(500)
b1.getstatus()

  
              
        
    