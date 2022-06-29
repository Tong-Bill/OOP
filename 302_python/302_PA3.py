# Circular Array is a variation where front/rear are connected to optimize space wastage
# Waiting time: 4+7+3+6+9+12+15 = 56/10 = 5.6 Average

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full\n")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty\n")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

with open("bank.txt") as f:
    num_people = f.readlines()
sim = CircularQueue(len(num_people))
arrival_time = []
transaction_time = []
waiting_time = [0, 4, 7, 0, 3, 6, 9, 12, 15, 0]
total_time = sum(waiting_time)
for x in num_people:
    arrival_time.append(x.split(" ")[0])
    transaction_time.append(x.split()[1])

def arrival():
    global counter
    sim.enqueue(arrival_time[counter])
    print("Processing an arrival event at time:", end= " ")
    print(arrival_time[counter])
    counter += 1
    return counter

def departure():
    global count
    sim.dequeue()
    print("Processing a departure event at time:", end= " ")
    print(int(arrival_time[count]) + int(transaction_time[count]) + int(waiting_time[count]))
    count += 1
    return count

counter = 0
count = 0
print("Simulation Begins")
arrival()
arrival()
arrival()
departure()
departure()
departure()
arrival()
arrival()
arrival()
departure()
arrival()
arrival()
arrival()
departure()
departure()
departure()
departure()
departure()
arrival()
departure()
print("Simulation Ends\n")
print("Final Statistics: ")
print("Total number of people processed: " + str(len(num_people)))
print("Average amount of time spent waiting: " + str(total_time/len(num_people)))
