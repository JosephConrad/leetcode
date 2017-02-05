# another clever in place solution
#    https://discuss.leetcode.com/topic/5056/any-shorter-o-1-space-solution


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        k, l = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(k):
            for j in range(l):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for index in rows:
            for i in range(l):
                matrix[index][i] = 0

        for index in cols:
            for i in range(k):
                matrix[i][index] = 0


if __name__ == "__main__":
    m = [[1, 2], [0, 3]]
    m = []
    Solution().setZeroes(m)
    print m
