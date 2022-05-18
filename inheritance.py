
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name},I am {self.age} years old, and I am {self.color}")

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

d = Dog("Bill", 34)
c = Cat("Zoomer", 40, "Brown")
d.show()
c.show()
