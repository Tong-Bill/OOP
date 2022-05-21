import os.path

def menu():
    print("-------------------------")
    print("0. Exit Program")
    print("1. Load Data")
    print("2. Display Wind Data")
    print("3. Wind Statistics")
    print("4. Add Data")
    print("5. Remove All Data")

def addWindData():
    f = open("wind.txt", "a+")
    item = int(input("How many wind data items would you like to add? "))
    count = 0
    while count < item:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        speed = float(input("Wind Speed: "))
        direction = input("Wind direction: ")
        x = direction.upper()
        items = count + 1
        array = [str(items) + " ", str(speed) + " ", str(x)]
        f.writelines(array)
        count += 1
    f.close()

def calcWindStats():
    f = open("wind.txt", "r")
    lines = f.readlines()
    speed = []
    direction = []
    for x in lines:
        speed.append(x.split(" ")[1])
        direction.append(x.split()[2])
    total_speed = 0
    for e in speed:
       total_speed = total_speed + float(e)
    avg_speed = str(total_speed / len(lines))
    frequent = max(direction, key=direction.count)
    print(f"Average speed: {avg_speed}")
    print(f"Most frequent wind direction: {frequent}")

def loadWindData(lines):
    file = os.path.exists("wind.txt")
    if file == True:
        f = open("wind.txt", "r")
        f.seek(0)
        lines = len(f.readlines())
        f.close()
        return lines
    else:
        print("The File does not exist.")
        raise SystemExit

def displayWindData():
    f = open("wind.txt", "r")
    lines = f.readlines()
    print("------------------------")
    print("Item # | Wind Speed | Wind Direction")
    items = []
    speed = []
    direction = []
    for x in lines:
        items.append(x.split(" ")[0])
        speed.append(x.split(" ")[1])
        direction.append(x.split()[2])
    for e in zip(items, speed, direction):
        print("{} {: >14} {: >10}".format(*e))
    f.close()

while True:
    menu()
    userChoice = int(input("Select an option: "))
    if userChoice == 0:
        raise SystemExit
    elif userChoice == 1:
        lines = 0
        loadWindData(lines)
        print("Number of data items: " + str(loadWindData(lines)))
    elif userChoice == 2:
        displayWindData()
    elif userChoice == 3:
        calcWindStats()
    elif userChoice == 4:
        addWindData()
    elif userChoice == 5:
        f = open("wind.txt", "r+")
        f.truncate(0)
        f.close()
    else:
        print("Invalid option, try again.")
