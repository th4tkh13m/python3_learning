class Item(): 

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight =weight

    def getName(self):
        """Return the name of an item"""
        return self.name

    def getValue(self):
        """Return the value of an item"""
        return self.value

    def getWeight(self):
        """Return the weight of an item"""
        return self.weight

    def negative_of_weight(self):
        """Return the negative value of weight"""
        return -self.getWeight()

    def ratio_of_value_weight(self):
        """Return the value/weight ratio of an item
           If the weight is equal to zero, return an error
        """
        try:
            return self.getValue()/self.getWeight()
        except ZeroDivisionError:
            return 'Cannot divide by 0!'

    def __str__(self):
        return self.getName() + f' has the value of {self.getValue()} and the weight of {self.getWeight()}'


class Player():

    def __init__(self, name):
        self.name = name
        self.value = 0
        self.storage = 20
        self.capacity = self.storage

    def getName(self):
        """Return Player's name"""
        return self.name

    def getCapacity(self):
        """Return Player's available storage"""
        return self.capacity

    def updateCapacity(self, capacity):
        """Update the Player's bag capacity"""
        self.capacity = capacity

    def upgradeStorage(self, size):
        """Upgrade the Player's storage using Shop"""
        self.storage += size

    def getMoney(self):
        """Return the player's money"""
        return self.value

    def updateMoney(self, amount):
        """Update the player's money"""
        self.value += amount

    def __str__(self):
        return f'Player {self.getName}: \nMoney: {self.getMoney}\nAvailable Storage:{self.getCapacity}'


class Shop():

    def __init__(self):
        pass
