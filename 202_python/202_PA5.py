
class Pet:
    def __init__(self, name, legs, tail):
        self.name = name
        self.legs = legs
        self.tail = tail

class Cat(Pet):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)

    def pounce(self):
        if self.legs > 2:
            print("RAWR!")
        else:
            print("meow")

class Fish(Pet):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)

    def swim(self):
        if self.tail == True:
            print("Just keep swimming!")
        else:
            print("glub glub")

class Bird(Pet):
    def __init__(self, name, legs, tail):
        super().__init__(name, legs, tail)

    def fly(self):
        if self.tail == True:
            print("Fly like the wind!")
        else:
            print("hop along")

c = Cat("Wick", 4, True)
f = Fish("Neemo", 0, True)
b = Bird("Greg", 2, True)

c.pounce()
f.swim()
b.fly()