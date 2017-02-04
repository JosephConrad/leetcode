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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy, dummy.next = ListNode(head.val - 1), head
        prev, curr = dummy, head

        while curr:
            if prev.val == curr.val:
                prev.next, curr = curr.next, curr.next
            else:
                prev, curr = prev.next, curr.next
        return dummy.next


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(10)
    l.next.next.next = ListNode(41)
    print Solution().deleteDuplicates(l)
