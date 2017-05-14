from random import randint

#https://gregable.com/2007/10/reservoir-sampling.html

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.l = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        length = 0
        head = self.l
        while head:
            head = head.next
            length += 1
        head = self.l
        for i in range(randint(0, length - 1)):
            head = head.next
        return head.val


if __name__ == "__main__":
    # Your Solution object will be instantiated and called as such:
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    obj = Solution(l)
    param_1 = obj.getRandom()
    print param_1
