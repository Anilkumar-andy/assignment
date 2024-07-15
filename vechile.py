traffic_light = "Green"
speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."
        print(message)

class Car(Vehicle):
    def __init__(self,make_of_the_car) -> None:
        self.make=make_of_the_car
        
    def start_engine(self):
        message ="Car engine started."
        print(message)
        
class Bike(Vehicle):
    def __init__(self,type_of_bike):
        self.type = type_of_bike
        
    def start_engine(self):
        message = "Bike engine started"
        print(message)
        
        

car = Car(make_of_the_car="Toyota")
bike = Bike(type_of_bike="Mountain")
    

vehicles = (car, bike)
for vehicle in vehicles:
    vehicle.start_engine()


def main():
    print(f"Global variable traffic_light: {traffic_light}")
    print(f"Module-level variable speed_limit: {speed_limit}\n")
    

#function will run only if it current file is run if this file is imported it won't
if __name__ == "__main__":    
    main()
