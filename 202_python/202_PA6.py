# Extended version of PA5, with classes in separate file for demonstration
import pet

def getCat():
    animal_name = input("Name: ")
    animal_legs = input("Number of legs: ")
    animal_tail = input("Presence of tail(yes or no): ")
    cat_info = pet.Cat(animal_name, animal_legs, animal_tail)
    return cat_info

def getFish():
    animal_name = input("Name: ")
    animal_legs = input("Number of legs: ")
    animal_tail = input("Presence of tail(yes or no): ")
    fish_info = pet.Fish(animal_name, animal_legs, animal_tail)
    return fish_info

def getBird():
    animal_name = input("Name: ")
    animal_legs = input("Number of legs: ")
    animal_tail = input("Presence of tail(yes or no): ")
    bird_info = pet.Bird(animal_name, animal_legs, animal_tail)
    return bird_info

def feedPet():
    # We could print directly from this function, but we are asked to return instead
    feed = input("What kind of food would you like to feed your pet? ")
    return feed

while True:
    print("Select Pet to manage: ")
    print("1.   Cat")
    print("2.   Fish")
    print("3.   Bird")
    print("4.   EXIT")
    userChoice = int(input())

    if userChoice == 1:
        myCat = getCat()
        catfood = feedPet()
        myCat.eat()
        print(catfood)
        myCat.pounce()
    elif userChoice == 2:
        myFish = getFish()
        fishfood = feedPet()
        myFish.eat()
        print(fishfood)
        myFish.swim()
    elif userChoice == 3:
        myBird = getBird()
        birdfood = feedPet()
        myBird.eat()
        print(birdfood)
        myBird.fly()
    elif userChoice == 4:
        break
    else:
        print("Invalid option, try again.")
