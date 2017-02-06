

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        return num == 1


if __name__ == "__main__":
    print Solution().isUgly(0)
    print Solution().isUgly(2147483648)
    print Solution().isUgly(-14)
    print Solution().isUgly(15)
    print Solution().isUgly(-7)
