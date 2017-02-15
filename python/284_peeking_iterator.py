# Below is the interface for Iterator, which is already defined for you.


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return len(self.nums) != 0

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        return self.nums.pop(0)


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_element = None
        self.has_peeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.has_peeked:
            self.peeked_element = self.iterator.next()
            self.has_peeked = True
        return self.peeked_element

    def next(self):
        """
        :rtype: int
        """
        if not self.has_peeked:
            return self.iterator.next()
        result = self.peeked_element
        self.has_peeked = False
        self.peeked_element = None
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_peeked or self.iterator.hasNext()


if __name__ == "__main__":
    # Your PeekingIterator object will be instantiated and called as such:
    nums = [1, 2, 3]
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()  # Get the next element but not advance the iterator.
        print val
        print iter.next()  # Should return the same value as [val].
