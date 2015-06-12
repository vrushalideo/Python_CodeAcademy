class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    
    def display_car(self):
        print "This is a %s %s with %r MPG." %(self.color, self.model, self.mpg)
        
    def drive_car(self):
        self.condition = "used" 
    
class ElectricCar(Car):
    def __init__(self,model,color,mpg,battery_type):
        super(ElectricCar,self).__init__(model,color,mpg)
        self.battery_type = battery_type
    
    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("Accord", "Grey", 34, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition

