# Given a linked list, remove the n-th node from the end of list and return its head.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)

# Naive approach:
# traverse to get length of list
# traverse again up until the nth to last node and remove it


def removeNth(head, n):
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    # to_remove is the node index we want to remove
    to_remove = length - n
    curr = head
    # if to_remove is the head
    if to_remove == 0:
        # return the heads next as the head
        return curr.next

    i = 1
    # sets curr to be the node before the node we want to remove
    while i < to_remove:
        curr = curr.next
        i += 1
    curr.next = curr.next.next
    return head


new_head = removeNth(node, 2)

curr = new_head
while curr:
    print(curr.val)
    curr = curr.next


# Better approach:
# have a slow pointer and a fast pointer
# fast pointer goes to position + 1

# def removeNth(head, n):
#     # dummy_head.next is reference to head
#     dummy_head = Node(0)
#     dummy_head.next = head

#     slow = dummy_head
#     fast = dummy_head

#     # fast will equal the node that is before the node we want to remove
#     for i in range(n + 1):
#         fast = fast.next
#     # slow will equal the node that is before the node we want to remove
#     while fast:
#         slow = slow.next
#         fast = fast.next

#     slow.next = slow.next.next

#     return dummy_head.next


# new_head = removeNth(node, 2)

# curr = new_head
# while curr:
#     print(curr.val)
#     curr = curr.next
