class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n is not 0:
            shift = (n - 1) % 26
            result += chr(ord('A') + shift)
            n -= shift
            n /= 26
        return ''.join(reversed(result))


if __name__ == '__main__':
    for i in range(1, 30):
        print Solution().convertToTitle(i)
