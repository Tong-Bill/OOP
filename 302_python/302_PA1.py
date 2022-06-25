# Linked list advantages: Dynamic array & ease of insertion/deletion
# Disadvantages: No random access, extra memory space for ptr, not cache friendly

def menu():
    print("1.   Add Item")
    print("2.   Delete Item")
    print("3.   Show # of items")
    print("4.   Show All Items")
    print("0.   EXIT")
    return int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the beginning of List
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Insert node after a given prev_node
    def insert(self, prev_node, new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert node at the end of List
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
            last.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key is not in linked list
        if (temp == None):
            return

        # Unlink node from Linked List
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while (temp):
            print(" %s" % (temp.data)),
            temp = temp.next

    def itemCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        print(f"Number of items: {count}")

llist = LinkedList()
while True:
    userChoice = menu()
    if userChoice == 1:
        push_data = input("Input data: ")
        # Can be changed to insert in different locations
        # Currently set to be inserted at beginning
        llist.push(push_data)
    elif userChoice == 2:
        remove_data = input("Remove data: ")
        llist.deleteNode(remove_data)
    elif userChoice == 3:
        llist.itemCount()
    elif userChoice == 4:
        llist.printList()
    elif userChoice == 0:
        break
    else:
        print("Invalid Option.")
        break


