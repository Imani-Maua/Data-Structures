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
        return newNode

 #O(1)
    
    def insertAtBeginning(self,x):
        newNode = Node(x)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode 
        return newNode

#worst case: O(n) 
    
    def insertMiddle(self, target, x):
        current = self.head
        while current:
            if current.data == target:
                newNode = Node(x)
                newNode.next = current.next
                current.next = newNode
                return self.head
            current = current.next
        print(f'Value {target} has not been found')
        return self.head

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
        return self.head

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
    

def addNodes():
    numbers = []
    while True:
        value = input('Please enter a number or q to quit:')
        if value.lower() == 'q':
            break
        try:
            num = int(value)
            numbers.append(num)
        except:
            print('please enter a valid number')
            continue
    return numbers

def addNodesAtEnd():
    linkedlist = LinkedList()
    nodes = addNodes()
    for node in nodes:
        linkedlist.insertAtEnd(node)
    return linkedlist

def addNodesAtBeginning():
    linkedlist = LinkedList()
    nodes = addNodes()
    for node in nodes:
        linkedlist.insertAtBeginning(node)
    return linkedlist




# Demo: inserting nodes at the end
print("\n=== Insert at End ===")
ll_end = addNodesAtEnd()
print("Linked List (end insert):")
ll_end.traverse()

# Demo: inserting nodes at the beginning
print("\n=== Insert at Beginning ===")
ll_start = addNodesAtBeginning()
print("Linked List (start insert):")
ll_start.traverse()

# Demo: inserting in the middle
print("\n=== Insert in Middle ===")
target_val = int(input("Enter the value after which to insert: "))
new_val = int(input("Enter the new value to insert: "))
ll_end.insertMiddle(target_val, new_val)
ll_end.traverse()

# Demo: deleting a node
print("\n=== Delete Node ===")
del_val = int(input("Enter the value to delete: "))
ll_end.deleteNode(del_val)
ll_end.traverse()

# Demo: reversing the list
print("\n=== Reverse List ===")
ll_end.reverseLinkedList()
ll_end.traverse()
