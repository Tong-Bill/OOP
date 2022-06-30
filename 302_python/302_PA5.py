# Deviating from guide for demonstration purposes of trees
# https://www.youtube.com/watch?v=lFq5mYUWEBk
import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add_child(self, data):
        # If value already exists, discard
        if data == self.data:
            return
        # If new data less than current node, add to left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)

    def getHeight(self):
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left:
            return 1 + self.left.getHeight()
        elif self.right:
            return 1 + self.right.getHeight()
        else:
            return 1

    def inOrder(self):
        elements = []
        if self.left:
            elements += self.left.inOrder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrder()
        return elements

    def preOrder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrder()
        if self.right:
            elements += self.right.preOrder()
        return elements

    def postOrder(self):
        elements = []
        if self.left:
            elements += self.left.postOrder()
        if self.right:
            elements += self.right.postOrder()
        elements.append(self.data)
        return elements

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

def main():
    random_list = []
    for x in range(0, 25):
        n = random.randint(1, 200)
        random_list.append(n)
    bst = build_tree(random_list)

    print("preorder BST:", end=" ")
    print(bst.preOrder())
    print("inorder BST:", end=" ")
    print(bst.inOrder())
    print("postorder BST:", end=" ")
    print(bst.postOrder())
    print("BST height:", end=" ")
    print(bst.getHeight())

if __name__ == "__main__":
    main()
