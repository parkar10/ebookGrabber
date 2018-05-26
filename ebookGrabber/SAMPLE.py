class shero():
    def __init__(self,name):
        self.name = name
        print('you\'re',self.name)
        self.transform = 3
    def change(self,name):
        self.name = name
        if self.transform > 0:
            print('you\'re transformed into ', self.name)
            self.transoform -=1
        else:
            print("shit all lives are used")
class enemy(shero):
    def __init__(self, name):

        print("im ",name, " but im enemy")


sm = enemy("batman")
print(sm.transoform)
#sm.change("batman")

