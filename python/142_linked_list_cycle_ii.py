# Definition for singly-linked list.
# More details: https://jincheng8841.gitbooks.io/leetcode-note/content/142_linked_list_cycle_ii.html


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None


class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                nodes = set()
                nodes.add(slow)
                while slow.next != fast:
                    slow = slow.next
                    nodes.add(slow)
                l = head
                while l not in nodes:
                    l = l.next
                return l
        return None


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    print Solution().detectCycle(l)

    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = l.next.next
    print Solution().detectCycle(l)
    l = ListNode(1)
    print Solution().detectCycle(l)
    l = ListNode(1)
    l.next = ListNode(2)
    print Solution().detectCycle(l)
    l = None
    print Solution().detectCycle(l)
