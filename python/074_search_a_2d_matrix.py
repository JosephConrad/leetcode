class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:
            return False
        i = self.lowerbound([row[0] for row in matrix], 0, len(matrix) - 1, target)
        return self.binsearch(matrix[i], 0, len(matrix[i]) - 1, target)

    def binsearch(self, a, l, r, target):
        m = (l + r) / 2
        if l > r:
            return False
        if a[m] == target:
            return True
        elif a[m] > target:
            return self.binsearch(a, l, m - 1, target)
        return self.binsearch(a, m + 1, r, target)

    def lowerbound(self, a, l, r, target):
        m = (l + r) / 2
        if l > r:
            return r
        if a[m] <= target:
            return self.lowerbound(a, m + 1, r, target)
        if a[m] > target:
            return self.lowerbound(a, l, m - 1, target)


if __name__ == "__main__":
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 20)
    print Solution().searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 10)
Se