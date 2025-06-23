class Railway:
    formType  = "Railwayform"  

    def getInfo(self):
        print(f"The Name = {self.name}")
        print(f"The Train = {self.train}")


r1 = Railway()
r1.name = "Komal"
r1.train = "chennai express"
r1.getInfo()