# 122. Best Time to Buy and Sell Stock II   Add to List QuestionEditorial Solution  My Submissions

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
#  (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple
#  transactions at the same time (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1, len(prices)):
            diff += max(0, prices[i] - prices[i - 1]) 

        return result


if __name__ == "__main__":
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])
    print Solution().maxProfit([1])
    print Solution().maxProfit([1, 4, 2])
    print Solution().maxProfit([])
