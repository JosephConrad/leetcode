class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


if __name__ == "__main__":
    print Solution().isPerfectSquare(16)
    # 16 = 1 + 3+ 5 + 7
