# 21. Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list. The new list
#   should be made by splicing together the nodes of the first two lists.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = start = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return start.next

if __name__ == "__main__":
    list1 = ListNode(4)
    list1.next = ListNode(6)
    list2 = ListNode(5)
    list2.next = ListNode(8)
    print Solution().mergeTwoLists(list1, list2)
    print Solution().mergeTwoLists(None, ListNode(0))
