
class Time:
    def __init__(self, hour, minute, second, millisecond):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond

    def getClockTime(self):
        userInput = input("hour, minute, second, millisecond separated by a space: ")
        array = userInput.split(" ")
        if len(array) != 4:
            print("Invalid number of inputs")
            raise SystemExit
        else:
            try:
                self.hour = int(array[0])
                self.minute = int(array[1])
                self.second = int(array[2])
                self.millisecond = int(array[3])

                if 0 <= self.hour <= 24:
                    if 0 <= self.minute <= 60:
                        if 0 <= self.second <= 60:
                            if 0 <= self.millisecond <= 1000:
                                return True, array
                            else:
                                print("Invalid milliseconds")
                                return False
                        else:
                            print("Invalid seconds")
                            return False
                    else:
                        print("Invalid minutes")
                        return False
                else:
                    print("Invalid hours")
                    return False
            except:
                print("Invalid input type")
                return False

    def display(self):
        print("Time passed is " + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second) + "." + str(self.millisecond))

    def calcHoursWorked(self):
        # We could import numpy and use subtract operation instead
        result = [int(y) - int(x) for x, y in zip(clockIn[1], clockOut[1])]
        # Make sure there are no negatives
        try:
            self.hour = int(result[0])
            self.minute = int(result[1])
            self.second = int(result[2])
            self.millisecond = int(result[3])

            if self.hour < 0:
                self.hour += 24
                if self.minute < 0:
                    self.hour -= 1
            if self.minute < 0:
                self.minute += 60
                if self.second < 0:
                    self.minute -= 1
            if self.second < 0:
                self.second += 60
            if self.millisecond < 0:
                self.millisecond += 1000
            self.display()
        except:
            print("Invalid Time.")
            return None

getTime = Time(0, 0, 0, 0)
print("--Clock-In Time--")
clockIn = getTime.getClockTime()
if clockIn == False:
    raise SystemExit
print("--Clock-Out Time--")
clockOut = getTime.getClockTime()
if clockOut == False:
    raise SystemExit
newTime = getTime.calcHoursWorked()
