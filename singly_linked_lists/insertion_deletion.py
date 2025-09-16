class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

#this insertion has a time complexity of O(n)
def insertAtEnd(head, x):
    newNode = Node(x)
    if not head:
        return newNode
    current = head
    while current.next:
        current = current.next
    current.next = newNode
    return head

#this insertion has a time complexity of O(1)
def insertAtBeginning(head, x):
    newNode = Node(x)
    newNode.next = head 
    return newNode

#the worst case time complexity for this insertion is O(n) where we have to traverse the entire list
def insertMiddle(head, target, x):
    current = head
    while current:
        if current.data == target:
            newNode = Node(x)
            newNode.next = current.next
            current.next = newNode
            return head
        current = current.next
    print(f'Value {target} has not been found')
    return head

def traverse(head):
    current = head
    while current:
        print(current.data)
        current = current.next

def addNodes():
    numbers = []
    while True:
        value = input('Please enter a number or q to quit:')
        if value.lower() == 'q':
            break
        try:
            num = int(value)
        except:
            print('please enter a valid number')
            continue
        numbers.append(num)
    return numbers

def addNodesAtEnd():
    linkedlist = None
    nodes = addNodes()
    for node in nodes:
        linkedlist = insertAtEnd(linkedlist, node)
    return linkedlist

def addNodesAtBeginning():
    linkedlist = None
    nodes = addNodes()
    for node in nodes:
        linkedlist = insertAtBeginning(linkedlist, node)
    return linkedlist

# if we are deleting the head, time complexity is O(1), otherwise worst case, where we have to traverse the entire list is O(n)
def deleteNode(head, value):
    if not head:
        print("This list is empty!")
        return head
    if head.data == value:
        head = head.next
    
    current = head
    while current.next and current.next.data != value:
        current = current.next
    
    if current.next:
        current.next = current.next.next
    else:
        print("Node not found!")
    return head

#demo for inserting nodes at the end
insert_end = addNodesAtEnd()
print("Linked List End Insert:")
traverse(insert_end)

#demo for inserting nodes at the beginning
insert_start = addNodesAtBeginning()
print("Linked List Start Insert:")
traverse(insert_start)

#demo for inserting a node after a certain node
insert_after = insertMiddle(insert_end, 30, 35)
print("Linked List Middle Insert:")
traverse(insert_after)

#demo for deleting a node
delete_node = deleteNode(insert_after, 30)
print("List with deleted Node:")
traverse(delete_node)