
# A @classmethod is a method bound to a class rather than an object
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def num_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Bean")
p2 = Person("Shelly")
print(Person.num_people())

# With @staticmethod, no need to create an instance like M = math
class Math:
    @staticmethod
    def add5(x):
        return x + 5
print(Math.add5(5))

