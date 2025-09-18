
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next.next.next = ListNode(9)



l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

def addTwoNumbers(l1, l2):
    carry = 0
    p1 = l1
    p2 = l2
    head = None
    curr = None

    while p1 is not None or p2 is not None:
        val1 = p1.val if p1 is not None else 0
        val2 = p2.val if p2 is not None else 0
        value = val1 + val2 + carry
        carry = value // 10
        value %= 10
        newNode = ListNode(value)

        if not head:
            head = newNode
            curr = newNode
        else:
            curr.next = newNode
            curr = newNode

        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
    if carry > 0:
        curr.next = ListNode(carry)
    return head
    


res = addTwoNumbers(l1, l2)

curr = res
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")