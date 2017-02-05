import heapq
import operator


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


class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        n = len(profits)
        gain = zip(capital, profits)
        gain.sort(key=operator.itemgetter(0))
        heap, j = MaxHeap(), 0

        while j < n and gain[j][0] <= w:
            heap.heappush(gain[j][1])
            j += 1

        while k > 0 and len(heap) > 0:
            w += heap.heappop()
            while j < n and gain[j][0] <= w:
                heap.heappush(gain[j][1])
                j += 1
            k -= 1
        return w


if __name__ == "__main__":
    print Solution().findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1])
