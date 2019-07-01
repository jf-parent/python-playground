from pytest import set_trace

class ListNode:
    def __init__(self, x, next_):
        self.val = x
        self.next = next_
    def __repr__(self):
        return f"Node<val: {self.val}>"

    def print(self):
        h = self
        while h.next:
            print(h, end=' => ')
            h = h.next

n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
head = ListNode(0, n1)

def recur_reverse_singly_linked_list(head):
    if not head:
        return -1
    else:
        def recur(h):
            if h.next:
                nh, t = recur(h.next)
                t.next = h
                t = h
                return nh, t
            else:
                return h, h
        nh, t = recur(head)
        t.next = None
        return nh

"""
new_head = recur_reverse_singly_linked_list(head)
new_head.print()
"""

def iter_reverse_singly_linked_list(head):
    c = head
    p = None
    while c:
        t = c.next
        c.next = p
        p = c
        c = t
    return p

new_head = iter_reverse_singly_linked_list(head)
new_head.print()
