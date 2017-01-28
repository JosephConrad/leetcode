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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(None, head)

    def reverse(self, acc, head):
        if head is None:
            return acc
        tail = head.next
        head.next = acc
        return self.reverse(head, tail)


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    print Solution().reverseList(l)
    l = ListNode(1)
    print Solution().reverseList(l)