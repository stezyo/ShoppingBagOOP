class ShoppingBag():
    
    bag = []
    
    def showBag(self):
        print(self.bag)

    def addToBag(self, item):
        self.bag.append(item)
    
    def removeFromBag(self, item):
        if item not in self.bag:
            print("invalid entry")
        else:
            self.bag.remove(item)
