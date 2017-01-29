class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MAX = -1000000000
        b1, b2 = MAX, MAX
        s1, s2 = 0, 0
        for price in prices:
            b1 = max(b1, - price)
            s1 = max(s1, b1 + price)
            b2 = max(b2, s1 - price)
            s2 = max(s2, b2 + price)
        return s2


if __name__ == "__main__":
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])
    print Solution().maxProfit([1])
    print Solution().maxProfit([1, 2, 3, 0, 2])
    print Solution().maxProfit([1, 3, 2, 7])
    print Solution().maxProfit([])
