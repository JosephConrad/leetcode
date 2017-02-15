import heapq


class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __repr__(self): return str(self.val)


class MinHeap(object):
    def __init__(self): self.h = []

    def heappush(self, x): heapq.heappush(self.h, x)

    def heappop(self): return heapq.heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)

    def __repr__(self): return str(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self): return heapq.heappop(self.h).val

    def __getitem__(self, i): return self.h[i].val


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = MinHeap()
        self.min.heappush(10000000000000)
        self.max = MaxHeap()
        self.max.heappush(-10000000000000)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        median = self.findMedian()
        if len(self.min) == len(self.max):
            if num < median:
                self.max.heappush(num)
                self.min.heappush(self.max.heappop())
            else:
                self.min.heappush(num)

        elif len(self.min) == len(self.max) + 1:
            if num < median:
                self.max.heappush(num)
            else:
                self.min.heappush(num)
                self.max.heappush(self.min.heappop())

    def findMedian(self):
        """
        :rtype: float
        """
        return (self.max[0] + self.min[0]) / 2.0 if len(self.max) == len(self.min) else self.min[0] * 1.0


if __name__ == "__main__":
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    for elt in [1, 2, 3, 4, 5, 23, 53, 34, 34, 34, 57, 4, 6, 4, 4]:
        obj.addNum(elt)
        print obj.findMedian()
