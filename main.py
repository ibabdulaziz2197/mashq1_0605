# 1
class Car:
    def __init__(self, brand, year, speed, fuel):
        self.brand = brand
        self.year = year
        self._speed = speed
        self.__fuel = fuel

    def accelerate(self, x):
        self._speed += x

    def refuel(self, x):
        self.__fuel += x

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Speed: {self._speed}")
        print(f"Fuel: {self.__fuel}")


car1 = Car("BMW", "2020","100", "50")
car1.accelerate(20)
car1.refuel(10)
car1.show_info()
