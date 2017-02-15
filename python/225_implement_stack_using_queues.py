import Queue


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue.Queue()
        self.q1 = Queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while not self.q.empty():
            elem = self.q.get()
            if not self.q.empty():
                self.q1.put(elem)
        self.q, self.q1 = self.q1, self.q
        return elem

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while not self.q.empty():
            elem = self.q.get()
            self.q1.put(elem)
        self.q, self.q1 = self.q1, self.q
        return elem

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()


if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(5)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    print param_2
    print param_3
    print param_4
