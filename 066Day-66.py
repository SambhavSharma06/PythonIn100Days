#Instance variables vs Class variables in Python!!
#Instance variables
class Game:
    def __init__(self,name):
        self.name = name
    def Display(self):
        print(self.name)
Game1 = Game("RE7")
Game2 = Game("RE8")
Game2.name = ("REVillage")#Instance Variable thats why I can change it here and it will change for forever.
Game1.Display()
Game2.Display()
#Class variables
class WorkOut:
    GuyName = ("FlyFit")
    def __init__(self,name):
        self.name = name
    def Display(self):
        print(self.name)
WorkOut1 = WorkOut(WorkOut.GuyName)
print(WorkOut1.GuyName)
