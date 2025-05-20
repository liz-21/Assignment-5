# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

vehicles = [Car(), Plane()]

for v in vehicles:
    v.move()
