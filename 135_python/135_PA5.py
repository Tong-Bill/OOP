
def menu():
    print("-------------------------")
    print("0. Exit Program")
    print("1. Load Data")
    print("2. Display Wind Data")
    print("3. Wind Statistics")
    print("4. Add Data")

def loadWindData():
    pass
def displayWindData():
    pass
def calcWindStats():
    pass
def addWindData():
    f = open("wind.txt", "a+")
    item = int(input("How many wind data items would you like to add? "))
    count = 0
    while count < item:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        item_num = count + 1
        speed = float(input("Wind Speed: "))
        direction = input("Wind direction: ")
        x = direction.upper()
        # Need to restrict direction to N E S W only
        array = [str(item_num) + " ", str(speed) + " ", str(x)]
        f.writelines(array)
        count += 1
    f.close()

while True:
    menu()
    userChoice = int(input("Select an option: "))
    if userChoice == 0:
        raise SystemExit
    elif userChoice == 1:
        loadWindData()
    elif userChoice == 2:
        displayWindData()
    elif userChoice == 3:
        calcWindStats()
    elif userChoice == 4:
        addWindData()
    else:
        print("Invalid option, try again.")
