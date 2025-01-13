class car:
    def __init__(self, model="Toyota", year=2090, color="red", price=5000, engine_started = False):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.engine_started = engine_started
        
    def engine(self):
        return f"The engine is {self.model} model"
    
    def engine_start(self):
        self.engine_started = True
        return f"The engine has started? {self.engine_start} and its engine is {self.model} model"
    
    def engine_stop(self):
        self.engine_stop = True
        return f"the engine has stopped? {self.engine_start} and its engine is {self.model} model"
    
    def car_speed(self, speed):
        self.speed = speed
        return f"The car speed is {self.speed} km/h"


ferarri = car() #instance of car class
print(type(ferarri))  # <class '_main_.car>
ferarri.engine_start =True

print(ferarri.engine_start)

#ferarri.engine_start()
#print(ferarri.emgine_started)