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
# def linked_list_find(head, target):
#  result = None
#  current = head
#  while current is not None:
#    if(current.val == target):
#      result = True
#      break
#    result = False
#    current = current.next
#  return result

# def linked_list_find(head, target):
# current = head
#  while current is not None:
#    if current.val == target:
#      return True
#    current = current.next
#  return False


def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)


print(linked_list_find(a, "c"))
