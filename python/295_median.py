import segmenttree

class MedianFinder:
    def __init__(self):
        min_heap = []
        max_heap = []
        """
        Initialize your data structure here.
        """

    def addNum(self, num):
        pass
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """

    def findMedian(self):
        return 1
        """
        Returns the median of current data stream
        :rtype: float
        """


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

def main():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.findMedian()
    mf.addNum(3)
    mf.findMedian()
