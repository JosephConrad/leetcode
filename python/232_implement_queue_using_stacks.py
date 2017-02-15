class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = []
        self.second = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.first.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.second:
            return self.second.pop()
        self.move()
        return self.second.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.second:
            return self.second[-1]
        self.move()
        return self.second[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.second == [] and self.first == []

    def move(self):
        while self.first:
            self.second.append(self.first.pop())


if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(5)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print param_2
    print param_3
    print param_4
