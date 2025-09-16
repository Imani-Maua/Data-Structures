from singly_linked_lists.operations import LinkedList
from doubly_linked_lists.operations import DoublyLinkedList

class demo():
    def __init__(self, linkedlist_class):
        self.linkedlist_class = linkedlist_class  # store the class, not an instance

    def addNodes(self):
        numbers = []
        while True:
            value = input('Please enter a number or q to quit: ')
            if value.lower() == 'q':
                break
            try:
                num = int(value)
                numbers.append(num)
            except:
                print('Please enter a valid number')
                continue
        return numbers

    def addNodesAtEnd(self):
        linkedlist = self.linkedlist_class()  # create a fresh instance
        nodes = self.addNodes()
        for node in nodes:
            linkedlist.insertAtEnd(node) if hasattr(linkedlist, "insertAtEnd") else linkedlist.insert_at_end(node)
        return linkedlist

    def addNodesAtBeginning(self):
        linkedlist = self.linkedlist_class()  # create a fresh instance
        nodes = self.addNodes()
        for node in nodes:
            linkedlist.insertAtBeginning(node) if hasattr(linkedlist, "insertAtBeginning") else linkedlist.insert_at_beginning(node)
        return linkedlist


# ===== SINGLY LINKED LIST DEMO ======
print("\n===== SINGLY LINKED LIST DEMO ======")
sll_demo = demo(LinkedList)

print("\n=== Insert at End ===")
ll_end = sll_demo.addNodesAtEnd()
print("Linked List (end insert):")
ll_end.traverse()

print("\n=== Insert at Beginning ===")
ll_start = sll_demo.addNodesAtBeginning()
print("Linked List (start insert):")
ll_start.traverse()

print("\n=== Insert in the middle ===")
target_val = int(input("Enter the value after which to insert: "))
new_val = int(input("Enter the new value to insert: "))
ll_end.insertMiddle(target_val, new_val)
ll_end.traverse()

print("\n=== Delete Node ===")
del_val = int(input("Enter the value to delete: "))
ll_end.deleteNode(del_val)
ll_end.traverse()

print("\n=== Reverse List ===")
ll_end.reverseLinkedList()
ll_end.traverse()

# ===== DOUBLY LINKED LIST DEMO ======
print("\n===== DOUBLY LINKED LIST DEMO ======")
dll_demo = demo(DoublyLinkedList)

print("\n=== Insert at End ===")
dll_end = dll_demo.addNodesAtEnd()
print("Doubly Linked List (end insert, forward traversal):")
dll_foward_traversal = DoublyLinkedList().fowardTraversal()

dll_end = dll_demo.addNodesAtBeginning()
print("Doubly Linked List (end insert, backward traversal):")
dll_end.traverse_backward()

print("\n=== Insert at Beginning ===")
dll_start = dll_demo.addNodesAtBeginning()
print("Doubly Linked List (start insert, forward traversal):")
dll_start.traverse_forward()
print("Doubly Linked List (start insert, backward traversal):")
dll_start.traverse_backward()

print("\n=== Insert After Node ===")
target_val = int(input("Enter the value after which to insert: "))
new_val = int(input("Enter the new value to insert: "))

# find node by value
current = dll_end.head
while current and current.data != target_val:
    current = current.next
if current:
    dll_end.insert_after(current, new_val)
else:
    print("Target value not found.")

dll_end.traverse_forward()
dll_end.traverse_backward()

print("\n=== Delete Node ===")
del_val = int(input("Enter the value to delete: "))
dll_end.delete(del_val)
dll_end.traverse_forward()
dll_end.traverse_backward()

print("\n=== Reverse List ===")
dll_end.reverse()
print("Doubly Linked List (reversed, forward traversal):")
dll_end.traverse_forward()
print("Doubly Linked List (reversed, backward traversal):")
dll_end.traverse_backward()
