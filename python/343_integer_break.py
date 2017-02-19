class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return [0, 1, 1, 2][n]
        if n % 3 == 0: return pow(3, n / 3)
        if n % 3 == 1: return pow(3, n / 3 - 1) * 4
        if n % 3 == 2: return pow(3, n / 3) * 2


if __name__ == "__main__":
    print Solution().integerBreak(4)
    print Solution().integerBreak(10)
