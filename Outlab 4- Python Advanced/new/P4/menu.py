from menuitem import MenuItem

class Menu():
    def __init__(self,items):
        self.items=items


    def __str__(self):
        a=''
        for x in self.items :
            a += str(x) + "\n"
        return a

    def __len__(self):
        return len(self.items)


