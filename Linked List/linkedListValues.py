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
#def linked_list_values(head):
#  arr = []
#  current = head
#  while current is not None:
#    arr.append(current.val)
#    current = current.next
#  return arr

def linked_list_values(head):
  values = []
  fill_values(head, values)
  return values

def fill_values(head, values):
  if head is None:
    return
  values.append(head.val)
  fill_values(head.next, values)

print (linked_list_values(a))


