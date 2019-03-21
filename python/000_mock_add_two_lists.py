#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
        l3 = ListNode(0)
        last = l3

        overflow = 0
        while l1 or l2: 
            val1, val2 = 0, 0
            if l1: 
                val1 = l1.val
                l1 = l1.next
            if l2: 
                val2 = l2.val
                l2 = l2.next

            added = ( val1 + val2 + overflow ) % 10
            overflow = ( val1 + val2 + overflow ) // 10
 
            last.next = ListNode(added)
            last = last.next

        if overflow: 
            last.next = ListNode(overflow)

        return l3.next



if __name__ == "__main__":
    #(2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(Solution().addTwoNumbers(l1,l2))


    # 1->8 + 0 
    l1 = ListNode(1)
    l1.next = ListNode(8) 
    l2 = ListNode(0) 
    print(Solution().addTwoNumbers(l1,l2))
