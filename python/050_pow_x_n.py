class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                result *= x
            abs_n >>= 1
            x *= x
        return result if n > 0 else 1 / result


if __name__ == "__main__":
    print Solution().myPow(3, 5)
    print Solution().myPow(3, 3)
    print Solution().myPow(1, 5)
    print Solution().myPow(2, 10)
    print Solution().myPow(2, 4)
    print Solution().myPow(2, 2)
    print Solution().myPow(2.323, -2)
