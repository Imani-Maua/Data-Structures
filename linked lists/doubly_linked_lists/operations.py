class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    #O(1)
    def insertAtBeginning(self, x):
        newNode = Node(x)
        if self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

    
    def insertAtEnd(self, x):
        newNode = Node(x)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current

    def insertAfter(self, target, x):
        newNode = Node(x)
        if not target:
            print("Target cannot be None.")
            return
        newNode.next = target.next
        newNode.prev = target
        if target.next:
            target.next.prev = newNode
        target.next = newNode

    def fowardTraversal(self):
        current = self.head
        while current.next:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

    def backTraversal(self):
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print("None")

    def deleteNode(self, target):
        if not self.head:
            print("This list is empty!")
            return
        if self.head.data == target:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        current = self.head
        while current:
            if current.data == target:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
    
    def reversal(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev





        