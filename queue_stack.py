class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.storage.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.storage.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.storage[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.storage) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
