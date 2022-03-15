import random


# 1. Read about how to define a class in python, have a member variable & functions for class
from _distutils_hack import override


class Operation:
    # 2. Constructor of a class
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


# 5. Create a class, Car. Have attributes like weight, max_speed, number_of_wheels, service_dates(List of datetime)
# and methods like get_max_speed(), update_max_speed(), add_service_date(), get_service_dates() and
# other methods for fetching and modifying attribute values.


class Car:

    def __init__(self, weight, max_speed, number_of_wheels, service_dates):
        self.weight = weight
        self.max_speed = max_speed
        self.number_of_wheels = number_of_wheels
        self.service_dates = service_dates

    def get_max_speed(self):
        return self.max_speed

    def update_max_speed(self, max_speed):
        self.max_speed = max_speed

    def add_service_date(self, new_service_date):
        self.service_dates.append(new_service_date)

    def get_service_date(self):
        return self.service_dates

    def topspeed(self):
        print(f"The car's top speed is {max_speed}")


# 7. Extending a base class
class Volkswagen(Car):

    def __init__(self, weight, max_speed, number_of_wheels, service_dates):
        super().__init__(weight, max_speed, number_of_wheels, service_dates)

    def __init_subclass__(cls, **kwargs):

        # 8. Override a method
    def topspeed(self):
        print(f"The topspeed of Volkswagen is {max_speed} Km/hr")

# 10 Create a base class vehicle. Extend the class and create car and bus. Create object for these classes
class Vehicle:
    def __init__(self,wheel,drive):
        self.wheel = wheel
        self.drive = drive

    def move(self):
        print("The vehicle is moving forward")

    def breakk(self):
        print("The vehicle is cocming to idle")


class Bus(Vehicle):
    def __init__(self, wheel, drive):
        super().__init__(wheel, drive)


if __name__ == "__main__":
    # 3. Create an object of an class
    a = 6
    b = 7
    obj = Operation(a, b)
    # 4. Call the method to modify the member variable
    print(obj.add())
    weight = 1000
    max_speed = 100
    number_of_wheels = 4
    service_dates = ['12-01-2022', '02-02-2022', '15-04-2022']
    polo = Car(weight, max_speed, number_of_wheels, service_dates)
    print(polo.get_max_speed())
    polo.add_service_date('03-05-2022')
    print(polo.get_service_date())
    print(polo.topspeed())
    vento = Volkswagen(weight, max_speed, number_of_wheels, service_dates)
    # 9. Call an overwritten method and non overwritten method from the object of the extended
    print(vento.topspeed())
    print(vento.get_service_date())
    # creating object for bus class
    buss = Bus(4,"Front")

