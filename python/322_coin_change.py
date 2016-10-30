# 322. Coin Change
# You are given coins of different denominations and a total amount of money amount.
#   Write a function to compute the fewest number of coins that you need to make up that amount.
#   If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7fffffff
        tab = [INF] * (amount + 1)
        tab[0] = 0
        for i in range(amount + 1):
            if tab[i] is INF:
                continue
            for coin in coins:
                if i + coin <= amount:
                    tab[i + coin] = min(tab[i + coin], tab[i] + 1)
        return tab[amount] if tab[amount] is not INF else -1


if __name__ == "__main__":
    print Solution().coinChange([1, 2, 5], 11)
    print Solution().coinChange([2], 3)
