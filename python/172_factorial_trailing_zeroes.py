class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        div, result = 5, 0
        while n / div > 0:
            result += n / div
            div *= 5
        return result


if __name__ == '__main__':
    for i in range(1, 30):
        print Solution().trailingZeroes(i)
