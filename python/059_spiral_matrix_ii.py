class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        tab = [[0] * n for _ in range(n)]

        k = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while k <= n * n:

            for i in range(left, right + 1):
                tab[top][i] = k
                k += 1
            top += 1

            for i in range(top, bottom + 1):
                tab[i][right] = k
                k += 1
            right -= 1

            for i in range(right, left - 1, -1):
                tab[bottom][i] = k
                k += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                tab[i][left] = k
                k += 1
            left += 1

        return tab


if __name__ == "__main__":
    print Solution().generateMatrix(5)
