# 342. Power of Four
#
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        binary = map(int, "{0:b}".format(num))
        return binary[0] == 1 and len(binary[1:]) % 2 == 0 and sum(binary[1:]) == 0


if __name__ == "__main__":
    print Solution().isPowerOfFour(-2147483648)
    print Solution().isPowerOfFour(16)
