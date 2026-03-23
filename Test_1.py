class Vehical:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
class Car(Vehical):
    def __init__(self,brand , speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type
    def show_detail(self):
        print("Vehical brand is: ",self.brand)
        print("Top speed: ",self.speed)
        print("Fuel: ",self.fuel_type)
        

c = Car("BMW",400,"Petrol")
c.show_detail()