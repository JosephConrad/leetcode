class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        i = 0
        n = Solution.num_length(x)
        while i < n / 2:
            if self.nth(x, i) != self.nth(x, n - i - 1):
                return False
            i += 1
        return True

    def nth(self, number, n):
        return int((number / pow(10, n)) % 10)

    @staticmethod
    def num_length(n):
        if n == 0:
            return 1
        n, l = abs(n), 0
        while n > 0:
            n /= 10
            l += 1
        return l


if __name__ == "__main__":
    print Solution().isPalindrome(342234236)
    print Solution().isPalindrome(9876543456789)
    print Solution().isPalindrome(3443)
