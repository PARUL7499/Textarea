class railways:
    def getstatus(self):
        print(f"the name of train = {self.nameoftrain}")
        print(f" the available seats = {self.availableseats}") 
        print("===============")

    def booking(self,seats):
     if self.availableseats < seats:
        self.availableseats = self.availableseats - seats
        print("seats are available") 
     else:
        print("not enough seats")
        print("the available {available} seats!")
        print("========")

    def cancelation(self,seats):
     if self.availableseats > seats:
        self.availableseats = self.availableseats + seats
        print("seats are available")
     else:
        print("not enough seats")
        print("the available {available} seats!")
        print("=========")


r1 = railways()
r1.nameoftrain = "maharaja express"
r1.availableseats =12

r1.booking(6)
r1.getstatus()

r1.cancelation(4)
r1.getstatus()