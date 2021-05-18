class MenuItem():

    def __init__(self,name,cost,rating):
        self.name=name
        self.cost=cost
        self.rating=rating

    def __eq__(self, other):
        if isinstance(other, MenuItem):
            if self.name == other.name  and self.cost == other.cost and self.rating== other.rating :
                return True
            return False
        return NotImplemented

    def __lt__(self, other):
        return self.rating < other.rating

    def __str__(self):
        dis = "Item: " + self.name + ", Cost:" + str(self.cost) + ", Rating:" + str(float(self.rating))
        return dis

    def __hash__(self):
        return hash(self.rating)









