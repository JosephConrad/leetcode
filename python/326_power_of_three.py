import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n != 1:
            rest = n % 3
            if rest:
                return False
            n /= 3
        return True


class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else n == round(3 ** round(math.log(n, 3)))


if __name__ == "__main__":
    print Solution().isPowerOfThree(3)
