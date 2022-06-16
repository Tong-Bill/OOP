# This module is used in 202_PA6

class Pet:
    def __init__(self, name, legs, tail):
        self.name = name
        self.legs = legs
        self.tail = tail

    def eat(self):
        print("eating ")

class Cat(Pet):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)

    def pounce(self):
        if int(self.legs) > 2:
            print("RWAR!")
        else:
            print("meow")

    def eat(self):
        print("devouring my ")

class Fish(Pet):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)

    def swim(self):
        if self.tail == "Yes" or self.tail == "yes":
            print("Just keep swimming!")
        else:
            print("glub glub")

    def eat(self):
        print("slurping my ")

class Bird(Pet):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)

    def fly(self):
        if self.tail == "Yes" or self.tail == "yes":
            print("Fly like the wind!")
        else:
            print("hop along")

    def eat(self):
        print("pecking at my ")
