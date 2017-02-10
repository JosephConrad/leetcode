class Solution(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        size = n / 2 if n % 2 == 0 else n / 2 + 1
        for i in range(size):
            for j in range(i, n - i - 1):
                m[i][j], m[j][n - i - 1], m[n - i - 1][n - j - 1], m[n - j - 1][i] = m[n - j - 1][i], m[i][j], m[j][
                    n - i - 1], m[n - i - 1][n - j - 1]


class Solution2(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        return [list(reversed(x)) for x in zip(*m)]


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print Solution2().rotate(m)
    Solution().rotate(m)
    for elt in m:
        print elt

    m = [[1]]
    Solution().rotate(m)
    print m

    m = []
    Solution().rotate(m)
    print m

    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    Solution().rotate(m)
    for elt in m:
        print elt
