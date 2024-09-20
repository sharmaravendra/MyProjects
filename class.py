class Human:
    def  __init__(self,n,o):
        self.name=n
        self.occupation=o

    def do_wor(self):
        if self.occupation == "actor":
            print(self.name,"shoots a film")
        elif self.occupation == "tennis player":
            print(self.name,"plays Tennis")

    def speaks(self):
        print(self.name,"Says how are you")

tom=Human("tom cruise","actor")
tom.do_wor()
tom.speaks()

maria=Human("maria sarapova","tennis player")
maria.do_wor()
maria.speaks()