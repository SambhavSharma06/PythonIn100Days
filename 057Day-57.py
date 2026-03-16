#Classes and Objects in Python!!

class Introduction:
    Name = "Sambhav"
    Occupation ="Data Analyst"
    NetWorth = 100000000
    def info(self):
        print(f"{self.Name}\n{self.Occupation}\n{self.NetWorth}\n")

a = Introduction()
b = Introduction()
b.Name = "Sam"
b.Occupation = "Data Analyst"
b.NetWorth = 10000000000000

a.info()
b.info()