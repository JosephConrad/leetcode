import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._min = 1

    def push(self, item, priority):
        heapq.heappush(self._queue, (self._min * priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def empty(self):
        return self._queue == []


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy, heap = ListNode(-1), PriorityQueue()
        current = dummy

        for node in lists:
            if node:
                heap.push(node, node.val)

        while not heap.empty():
            node = heap.pop()

            if node.next:
                heap.push(node.next, node.next.val)
            current.next, current = node, node

        return dummy.next


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(10)
    l.next.next.next = ListNode(41)
    l1 = ListNode(4)
    l1.next = ListNode(5)
    l1.next.next = ListNode(7)
    l1.next.next.next = ListNode(9)
    l2 = ListNode(0)
    l2.next = ListNode(3)
    l2.next.next = ListNode(6)
    l2.next.next.next = ListNode(8)
    print Solution().mergeKLists([l, l1, l2])
