class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


def insertAtEnd(head, x):
    newNode = Node(x)
    if not head:
        return newNode
    current = head
    while current.next:
        current = current.next
    current.next = newNode
    return head

#this insertion has a time complexity of O(n)

def traverse(head):
    current = head
    while current:
        print(current.data)
        current = current.next


def addNodesAtEnd():
    linkedlist = None
    while True:
        value = input('Please enter a number or q to quit:')
        if value.lower() == 'q':
            break
        try:
            num = int(value)
        except:
            print('please enter a valid number')
            continue
        linkedlist = insertAtEnd(linkedlist, num)
    return linkedlist



addNodes = addNodesAtEnd()
print('Linked List:')
traversal = traverse(addNodes)

        