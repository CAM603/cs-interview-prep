class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    to_sort = []

    current = l1
    while current:
        to_sort.append(current.val)
        current = current.next

    current = l2
    while current:
        to_sort.append(current.val)
        current = current.next

    if not to_sort:
        return

    to_sort = sorted(to_sort)

    n = ListNode(to_sort.pop(0))

    current = n
    while to_sort:
        current.next = ListNode(to_sort.pop(0))
        current = current.next

    current = n
    while current:
        print(current.val)
        current = current.next

    return n


n3 = ListNode(4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

n6 = ListNode(4)
n5 = ListNode(3, n6)
n4 = ListNode(1, n5)

mergeTwoLists(n1, n4)
