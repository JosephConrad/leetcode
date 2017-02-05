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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        d1, d1.next = ListNode(0), head
        curr, prev, curr2 = d1.next, d1, None
        while curr:
            if curr.val >= x:
                prev.next = curr.next
                curr.next = curr2
                curr2 = curr
                curr = prev.next
            else:
                curr, prev = curr.next, curr

            if curr is None:
                # reverse the second list before joining it to the first one
                head2 = None
                while curr2:
                    curr2.next, head2, curr2 = head2, curr2, curr2.next
                prev.next = head2
                break
        return d1.next

if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(4)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(5)
    print Solution().partition(l, 3)
    l = ListNode(1)
    l.next = ListNode(2)
    print Solution().partition(l, 0)
