class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i / 2) for i in range(2 ** n)]


class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i >> 1 ^ i for i in range(1 << n)]


if __name__ == "__main__":
    print Solution().grayCode(2)

