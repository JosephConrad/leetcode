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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.list_length(headA)
        lenB = self.list_length(headB)
        if lenA > lenB:
            headA = self.move_head(headA, lenA - lenB)
        else:
            headB = self.move_head(headB, lenB - lenA)

        while headA is not headB:
            headB = headB.next
            headA = headA.next
        return headA

    def list_length(self, head):
        counter = 0
        while head:
            head = head.next
            counter += 1
        return counter

    def move_head(self, head, length):
        while length:
            head = head.next
            length -= 1
        return head


if __name__ == "__main__":
    l = ListNode(1)
    print Solution().getIntersectionNode(l, l)
    print Solution().getIntersectionNode(l, None)
