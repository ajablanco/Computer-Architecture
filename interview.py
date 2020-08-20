# """
# Implement remove_kth_node function that takes in an integer K and head of the linked list.
# 1. Remove the kth node in the linked list starting from HEAD and 
# return the head of the new linked list

# 2. Given the HEAD of a linked list, get the length of the linked list

# 3. Remove the kth node in the linked list starting from TAIL 

# -- Don't worry about edge cases for now
# Example
# 3 -> 4 -> 3 -> 2 -> 6 -> 1 -> 2 -> 6 -> None
# k = 4
# new_ll = remove_kth_node(k, head)
# Output:
# 3 -> 4 -> 3 -> 6 -> 1 -> 2 -> 6 -> None
# """


        
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
# Implement this
def remove_kth_node(k, head):
    cur = head
    prev = None
    while (k-1) != 0:
        prev = cur
        cur = cur.next
        k -= 1
    prev.next = cur.next
    return head
def get_len(head):
    cur = head
    count = 0
    while cur is not None:
        cur = cur.next
        count += 1
    return count
def remove_kth_node_from_tail(k, head):
    cur = head
    prev = None
    count = 0
    while cur is not None:
        prev = cur
        cur = cur.next
        count += 1
    val = count - k
    cur = head
    prev = None
    while (val) != 0:
        prev = cur
        cur = cur.next
        val -= 1
    prev.next = cur.next
    return head

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
new_llhead = remove_kth_node(4, a)
print_list(new_llhead)  # should return 3 -> 4 -> 3 -> 6 -> 1 -> 2 -> 6 -> None
print("")
new_lltail= remove_kth_node_from_tail(4, a)
print_list(new_lltail)  # 3 -> 4 -> 3 -> 1 -> 2 -> 6 -> None
print("")

# a0 HEX
# 0b1010 0000 BINARY


"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
Example:
Input: "((()))"
Output: True
Input: "[()]{}"
Output: True
Input: "({[)]"
Output: False
"""

def is_valid(string):
    char_count = {}
    true_count = 0
    false_count = 0
    temp = 0
    for el in string:
        if el not in char_count:
            char_count[el] = 1
        else:
            char_count[el] += 1
    for i in char_count:
        if i == "(":
            if ")" in char_count.keys() and char_count[i] == char_count[")"]:
                true_count += 1
            else:
                false_count += 1
        elif i == "[":
            if "]" in char_count.keys() and char_count[i] == char_count["]"]:
                true_count += 1
            else: 
                false_count += 1
        elif i == "{":
            if "}" in char_count.keys() and char_count[i] == char_count["}"]:
                true_count += 1
            else:
                false_count += 1
        elif i == ")" or i == "]" or i == "}":
            temp += 1
        else:
            false_count += 1      
    if false_count > 0:
        return False
    else:
        return True


print(is_valid("((()))"))  # True
print(is_valid("[()]{}"))  # True
print(is_valid("({[)]"))  # False