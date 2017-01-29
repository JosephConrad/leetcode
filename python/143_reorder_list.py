# Definition for singly-linked list.
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
    def reorderList(self, l):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if l is None:
            return l

        # find middle
        fast, slow, prev = l, l, None
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next

        # split list into two lists
        head, slow.next = slow.next, None

        # Reverse
        acc = None
        while head is not None:
            head.next, acc, head = acc, head, head.next


        # reorder
        head, head2 = l, acc
        while head and head2:
            temp = head.next
            head.next = head2
            head = temp
            temp2 = head2
            head2 = head2.next
            temp2.next = temp


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    Solution().reorderList(l)

    print l
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(6)
    Solution().reorderList(l)
    print l
    l = ListNode(1)
    Solution().reorderList(l)
    print l
    l = ListNode(1)
    l.next = ListNode(2)
    Solution().reorderList(l)
    print l
    l = None
    Solution().reorderList(l)
    print l
