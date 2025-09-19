class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = next

def mergeTwoLists(ls1, ls2):
    
    p1 = ls1
    p2 = ls2
    if not p1:
        return p2
    if not p2:
        return p1
    head = None
    curr = None
    while p1 and p2:
        if not head:
            if p1.val <= p2.val:
                head = ListNode(p1.val)
                curr = head
            else:
                head = ListNode(p2.val)
                curr = head
        else:
            if p1.val <= p2.val:
                newNode = ListNode(p1.val)
                curr.next  = newNode
                curr =newNode
                p1 = p1.next
            else:
                newNode = ListNode(p2.val)
                curr.next = newNode
                curr = newNode
                p2 = p2.next
    curr.next = p1 if p1 else p2
    return head


        