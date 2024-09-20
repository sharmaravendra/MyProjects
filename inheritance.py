class Vehicle:
    def general_usage(self):
        print("General usage: Transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Specific use: used for transport and family outing")
class MotorCycle(Vehicle):
    def __init__(self):
        print("I am Motor Cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Specific use: used for road trip and race")


c = Car()
# print(c.general_usage())
print(c.specific_usage())
b=MotorCycle()
print(b.specific_usage())

print(isinstance(c,Car))
print(isinstance(c,MotorCycle))

print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))

