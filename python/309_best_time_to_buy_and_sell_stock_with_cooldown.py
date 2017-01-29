# There are two actions: "buy" and "sell", so we can use two arrays to denote the max profit by
#   ending with these two actions.
#
# Define:
# buy[i]: the max profit at index i ending by the "buy" operation.
#   (note: not buy at the ith day, any time buy between the [0...i] ending with buy operation).
#
# sell[i]: the max profit at index i ending by the "sell" operation.
#
#
# For each buy[i], you can choose to have a rest, keep the max profit from the previous day buy[i-1].
#   Or, you can choose to buy, the max profit will be sell[i-2] + prices[i].
# For sell[i], you can also choose to have a rest, keep the profit from previous day sell[i-1],
#   or sell the stock, you will get buy[i-1] + prices[i].
#
# The transformation function is:
# buy[i] = max(buy[i-1], sell[i-2] - prices[i]);
# sell[i] = max(sell[i-1], buy[i-1] + prices[i]);


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices or n == 1:
            return 0
        buy = [0] * n
        buy[0] = -prices[0]
        sell = [0] * n
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i] if i >= 2 else -prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[-1]

if __name__ == "__main__":
    print Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print Solution().maxProfit([7, 6, 4, 3, 1])
    print Solution().maxProfit([1])
    print Solution().maxProfit([1, 2, 3, 0, 2])
    print Solution().maxProfit([1, 3, 2, 7])
    print Solution().maxProfit([])
