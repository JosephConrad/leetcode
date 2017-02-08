class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1 + ((num - 1) % 9) if num > 0 else 0


if __name__ == "__main__":
    print Solution().addDigits(0)
    print Solution().addDigits(-1)
    print Solution().addDigits(-9)
    print Solution().addDigits(-10)
    print Solution().addDigits(1)
    print Solution().addDigits(9)
    print Solution().addDigits(81)
    print Solution().addDigits(1000000000000)
