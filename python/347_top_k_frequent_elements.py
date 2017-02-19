from collections import defaultdict
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []

    # insert priority to -priority can change to max priority queue
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[1]

    def __str__(self):
        return str(self._queue)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pq, d, result = PriorityQueue(), defaultdict(int), []
        for elt in nums:
            d[elt] += 1
        for key, item in d.iteritems():
            pq.push(key, item)
        for _ in range(0, k):
            result.append(pq.pop())
        return result


if __name__ == "__main__":
    print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print Solution().topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5], 3)
    print Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
