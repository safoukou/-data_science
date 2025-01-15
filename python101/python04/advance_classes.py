# dictionaries and list
#dictionaries are a way to store information that is  connected in some way.
#A dictionary is a 






#creating a dictionary
alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0['points'])
print(alien_0)
#update the valeur
alien_0['points'] = 10
print(alien_0['points'])
print(alien_0)
#removing key-value pair
del alien_0['y_position']
print(alien_0)

#adding a new key-value pair
alien_0['y_position'] =  10

print(alien_0)

for key in alien_0:
    print(key)

for value in alien_0.values():
    print(value)

for keys, value in alien_0.items():
    print()

for keys, value in alien_0.items():
    print(f"key: {keys}, value : (value)")

#help remove the value at any press
alien_0["points"] -=2 #or alien_0["points"] = alien_0["points"]-2




class House:
    def __init__(self, owner, location, price, width, length, floor):
        self.owner =owner
        self.location = location
        self.price =price
        self.width = width
        self.length = length
        self.floor = floor
    def floor_area(self):
        return self.width*self.length

    def price_per_erea(self):
        return self.price /self.floor_erea()
    
    def house_info(self):
        return f"owner: {self.owner}, Location: {self.location}, price:{self.price},price per erea: {self.price_per_erea}"


jules_house = House("jules kasongo", "Djamena, Tchad, central Africa rupublic", 100000, 30, 60, 89)

class jules_skyskraper(House):
    def __init__(self, owner, location, price, width, length, floor):
        super().__init__(owner, location, price, width, length, floor)
        self.floor = floor 
    
    def floor_area(self):
        print(super().floor_erea())
        return super().floor_area()*self.floor



jules_skyskraper = jules_skyskraper("jules Dongmo", "Hemmingen, Germany", 1000000, 30, 40, 70)

print(jules_skyskraper.house_info())

#iheritance

class Calvin_skyskraper(jules_skyskraper):
    def __init__(self, owner, location, price, width, length, floor, color):
        super().__init__(owner, location, price, width, length, floor)
        self.color = color

    def house_info(self):
        return f"owner: {self.owner}, Location: {self.location}, price: {self.price}$, price per area: {self.price_per_area()}$, color:{self.color}, size: {self.size_per_erear}"

Calvin_skyskraper = Calvin_skyskraper("calvin le pain", "Brooklyn, New York", 10000000, 35, 40, 15, "Grey")

print(Calvin_skyskraper.house_info())
    