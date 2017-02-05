class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        k, l = len(matrix), len(matrix[0])

        lines = []
        for i in range(k - 1):
            lines.append(self.genLine(i, 0, matrix, l))

        for j in range(l):
            lines.append(self.genLine(k - 1, j, matrix, l))

        for i, line in enumerate(lines):
            if i % 2 == 1:
                lines[i] = line[::-1]

        return [item for sublist in lines for item in sublist]

    def genLine(self, i, j, matrix, l):
        acc = []
        while i >= 0 and j < l:
            acc.append(matrix[i][j])
            i -= 1
            j += 1
        return acc

if __name__ == "__main__":
    print Solution().findDiagonalOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
