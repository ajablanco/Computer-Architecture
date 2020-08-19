# """
# Implement remove_kth_node function that takes in an integer K and head of the linked list.
# Remove the kth node in the linked list starting from HEAD and 
# return the head of the new linked list
# -- Don't worry about edge cases for now
# Example
# 3 -> 4 -> 3 -> 2 -> 6 -> 1 -> 2 -> 6 -> None
# k = 4
# new_ll = remove_kth_node(k, head)
# Output:
# 3 -> 4 -> 3 -> 6 -> 1 -> 2 -> 6 -> None
# """

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# def print_list(head):
#     cur = head
#     while cur is not None:
#         if cur.next is not None:
#             print(f"{cur.data} -> ", end="")
#         else:
#             print(f"{cur.data} -> None", end="")
#         cur = cur.next
# # Implement this
# def remove_kth_node(k, head):
#     cur = head
#     prev = None
#     while (k-1) != 0:
#         prev = cur
#         cur = cur.next
#         k -= 1
#     prev.next = cur.next
#     return head
        



# a = Node(3)
# b = Node(4)
# c = Node(3)
# d = Node(2)
# e = Node(6)
# f = Node(1)
# g = Node(2)
# h = Node(6)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
# g.next = h



# new_llhead = remove_kth_node(4, a)
# print_list(new_llhead)  # should return 3 -> 4 -> 3 -> 6 -> 1 -> 2 -> 6 -> None







"""
Given the HEAD of a linked list, get the length of the linked list
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def print_list(head):
    cur = head
    while cur is not None:
        if cur.next is not None:
            print(f"{cur.data} -> ", end="")
        else:
            print(f"{cur.data} -> None", end="")
        cur = cur.next
def get_len(head):
    cur = head
    prev = None
    count = 0
    while cur is not None:
        prev = cur
        cur = cur.next
        count += 1
    return count
       
    
a = Node(3)
b = Node(4)
c = Node(3)
d = Node(2)
e = Node(6)
f = Node(1)
g = Node(2)
h = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
print(get_len(a)) # should print 8






