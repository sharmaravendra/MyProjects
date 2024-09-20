class Father():
    def skills(self):
        print("Gardning, Programming")
class Mother():
    def skills(self):
        print("Cooking, art")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")
c=Child()
c.skills()

