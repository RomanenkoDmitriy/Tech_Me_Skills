import time


#                1
class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = None
        self.weight = 0

    def move(self):
        print("Move")

    @staticmethod
    def stop():
        print("Stop")

    def birthday(self):
        self.age = self.age + 1


#                       2

class Truck(Auto):

    def __init__(self, brand, age, mark, max_long):
        super().__init__(brand, age, mark)
        self.max_long = max_long

    def move(self):
        print("Attentio")
        super().move()

    @staticmethod
    def load():
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Cur(Auto):

    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")


truck1 = Truck("Scania", 3, "sx2546", 14)
truck2 = Truck("Peterbilt", 2, "379", 12)

cur1 = Cur("BMW", 4, "m5", 222)
cur2 = Cur("Ford", 1, "F150 Raptor", 200)

truck1.stop()
truck1.move()
truck1.load()
print(f"age {truck1.age}")
truck1.birthday()
truck1.color = "Red"
truck1.weight = 10

print(f"brand {truck1.brand}")
print(f"age after {truck1.age}")
print(f" mark {truck1.mark}")
print(f" max_long {truck1.max_long}")
print(f"color {truck1.color}")
print(f"weight {truck1.weight}")

print("-------------------------------------------")

truck2.stop()
truck2.move()
truck2.load()
print(f"age {truck2.age}")
truck2.birthday()
truck2.weight = 9

print(f"brand {truck2.brand}")
print(f"age after {truck2.age}")
print(f" mark {truck2.mark}")
print(f" max_long {truck2.max_long}")
print(f"color {truck2.color}")
print(f"weight {truck2.weight}")

print("-------------------------------------------")

cur1.stop()
cur1.move()
print(f"age {cur1.age}")
cur1.birthday()
cur1.color = "Yellow"
cur1.weight = 2

print(f"brand {cur1.brand}")
print(f"age after {cur1.age}")
print(f" mark {cur1.mark}")
print(f" max_speed {cur1.max_speed}")
print(f"color {cur1.color}")
print(f"weight {cur1.weight}")

print("-------------------------------------------")

cur2.stop()
cur2.move()
print(f"age {cur2.age}")
cur2.birthday()
cur2.weight = 4

print(f"brand {cur2.brand}")
print(f"age after {cur2.age}")
print(f" mark {cur2.mark}")
print(f" max_speed {cur2.max_speed}")
print(f"color {cur2.color}")
print(f"weight {cur2.weight}")
