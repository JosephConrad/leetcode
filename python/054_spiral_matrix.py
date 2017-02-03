class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, n - 1, 0, m - 1
        result = []

        while left <= right and top <= bottom:

            if n == 1:
                return matrix[0]

            if m == 1:
                return list(zip(*matrix)[0])

            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for i in range(right, left - 1, -1):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for i in range(bottom - 1, top, -1):
                if left < right:
                    result.append(matrix[i][left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return result


if __name__ == "__main__":
    print Solution().spiralOrder([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print Solution().spiralOrder([[2, 3]])
    print Solution().spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print Solution().spiralOrder([[2], [3], [5]])
