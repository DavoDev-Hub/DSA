class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d


def get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index - 1)


#  current = head
#  currentIndex = 0
#  while current is not None:
#    if currentIndex == index:
#      return current.val
#    currentIndex += 1
#    current = current.next
#    return None

print(get_node_value(a, 2))
