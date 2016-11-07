class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n & (n - 1)


if __name__ == "__main__":
    print Solution().isPowerOfTwo(4)
    print Solution().isPowerOfTwo(0)
    print Solution().isPowerOfTwo(9)
    print Solution().isPowerOfTwo(-8)
