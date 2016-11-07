# 19. Remove Nth Node From End of List
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        cand = dummy = ListNode(0)
        dummy.next = head
        curr = head

        for _ in range(n):
            curr = curr.next

        while curr:
            curr, cand = curr.next, cand.next

        if cand == dummy:
            return cand.next.next

        cand.next = cand.next.next
        return head

if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    print Solution().removeNthFromEnd(l, 0)
    print Solution().removeNthFromEnd(l, 2)
    print Solution().removeNthFromEnd(l, 3)
    print Solution().removeNthFromEnd(l, 3)
