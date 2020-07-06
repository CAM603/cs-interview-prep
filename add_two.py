class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dic = {l1: [], l2: []}

    # put node values in a stack
    current = l1
    while current is not None:
        dic[l1].append(current.val)
        current = current.next

    current = l2
    while current is not None:
        dic[l2].append(current.val)
        current = current.next

    str_one = ""
    str_two = ""

    # pop from stack to unreverse number
    while len(dic[l1]) > 0:
        str_one += str(dic[l1].pop())
    while len(dic[l2]) > 0:
        str_two += str(dic[l2].pop())

    num = int(str_one) + int(str_two)

    num_list = [int(x) for x in str(num)]
    num_list.reverse()

    # create linked list representing new number
    root = None
    for i in range(len(num_list) - 1, -1, -1):
        temp = ListNode(0)
        temp.val = num_list[i]
        temp.next = root
        root = temp

    return root


c = ListNode(3)
b = ListNode(4, c)
a = ListNode(2, b)

g = ListNode(4)
f = ListNode(6, g)
e = ListNode(5, f)

addTwoNumbers(a, e)
