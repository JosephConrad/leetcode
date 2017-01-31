class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        return res if res < pow(2, 31) else 0


if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(100)
    print Solution().reverse(0)
    print Solution().reverse(9876543456789)
    print Solution().reverse(1563847412)
