# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        last = dummy
        overflow = 0
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + overflow
            node, overflow = ListNode(val % 10), val / 10
            last.next, last = node, node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if overflow:
            last.next = ListNode(overflow)
        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(2)
    list1.next = ListNode(4)
    list1.next.next = ListNode(3)
    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)
    print Solution().addTwoNumbers(list1, list2)
    list1 = ListNode(2)
    list1.next = ListNode(4)
    list1.next.next = ListNode(3)
    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(9)
    print Solution().addTwoNumbers(list1, list2)

