class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append((x, self.getMin() if self.stack and self.getMin() < x else x))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minimal = minStack.getMin()
    print minimal
    minStack.pop()
    top = minStack.top()
    print top
    minimal = minStack.getMin()
    print minimal
