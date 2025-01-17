#Dictionaries and list
#Dictionaries are a way to store information that is connected in some way.
#A dictionary is a collection of key-value pairs.
#Each key is connected to a value, and you can use a key to access the value associated with that key.
#A key’s value can be a number, a string, a list, or even another dictionary.
#In fact, you can use any object that you can create in Python as a value in a dictionary.
#In Python, a dictionary is wrapped in braces, {}, with
# a series of key-value pairs inside the braces, as shown

#Creating a dictionary
alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(alien_0['color'])
print(alien_0)
#updating a key-value pairs
alien_0["color"] ="Red"

print(alien_0['color'])

#Removing key-value pairs
del alien_0['y_position']

print(alien_0)

#Adding a new key-value pair
alien_0['z_position'] = 35

print(alien_0)

for key in alien_0:
    print(key)

for value in alien_0.values():
    print(value)

for keys, value in alien_0.items():
    print(f"Key: {keys}, Value: {value}")

alien_0["points"] -=2
alien_0["points"] = alien_0["points"]-2

print(alien_0)


class House:
    def __init__(self, owner, location, price, width, length):
        self.owner = owner
        self.location = location
        self.price = price
        self.width = width
        self.length = length

    def floor_area(self):
        return self.width*self.length

    def price_per_area(self):
        return self.price /self.floor_area()
    def house_info(self):
        return f"Owner: {self.owner}, Location: {self.location}, Price:{self.price}Euro, Price per area: {self.price_per_area()}"

_Jules_house = House("Jules Kasongo", "Djamena, Tchad, Central African Republic", 100000, 30, 40)

print(_Jules_house.house_info())

#Inheritance
class Jules_Skyskraper(House): #instantiation
    def __init__(self, owner, location, price, width, length, floor):
        super().__init__(owner, location, price, width, length)
        self.floor = floor

    def floor_area(self):
        print(super().floor_area())
        return super().floor_area()*self.floor


Jules_skyskraper = Jules_Skyskraper("Jules Dongmo", "Hemmingen, Germany", 1000000, 30, 40, 20)

print(Jules_skyskraper.house_info())

#Inheritance
class Calvin_skyskraper(Jules_Skyskraper):
    def __init__(self, owner, location, price, width, length, floor, color):
        super().__init__(owner, location, price, width, length, floor)
        self.color = color

    def house_info(self):
        return f"Owner: {self.owner}, Location: {self.location}, Price: {self.price}$, price per area: {self.price_per_area()}$, Color:{self.color}"

Calvin_skyskraper = Calvin_skyskraper("Calvin le pain", "Brooklyn, New York", 10000000, 35, 48, 15, "Grey")

print(Calvin_skyskraper.house_info())