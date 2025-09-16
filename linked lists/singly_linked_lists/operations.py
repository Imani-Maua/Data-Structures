class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

#O(n)
    
    def insertAtEnd(self, x):
        newNode = Node(x)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


 #O(1)
    
    def insertAtBeginning(self,x):
        newNode = Node(x)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode 


#worst case: O(n) 
    
    def insertMiddle(self, target, x):
        current = self.head
        while current:
            if current.data == target:
                newNode = Node(x)
                newNode.next = current.next
                current.next = newNode
            current = current.next
        print(f'Value {target} has not been found')

# O(n)
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

    
# deleting the head, O(1), otherwise worst case, O(n)
    
    def deleteNode(self, value):
        if not self.head:
            print("This list is empty!")
            return self.head
        if self.head.data == value:
            return self.head.next

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Node not found!")
    

#0(n)
    
    def reverseLinkedList(self):
        prev = None
        current = self.head
        self.tail = self.head  # old head becomes new tail
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    





