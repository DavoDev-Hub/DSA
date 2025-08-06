class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c


x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z


def zipper_lists(head_1, head_2):
    tail = head_1
    current1 = head_1.next
    current2 = head_2
    count = 0
    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next_1
        tail += 1
        count = +1

    if current1 is None:
        tail.next = current2
    if current2 is None:
        tail.next = current1

    return head_1


# def zipper_lists(head_1, head_2):
#     if head_1 is None and head_2 is None:
#         return None
#
#     if head_2 is None:
#         return head_1
#
#     if head_1 is None:
#         return head_2
#
#     next_1 = head_1.next
#     next_2 = head_2.next
#
#     head_1.next = head_2
#     head_2.next = zipper_lists(next_1, next_2)
#
#     return head_1
