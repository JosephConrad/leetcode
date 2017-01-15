class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        triangle = [[1]]
        for i in range(2, numRows + 1):
            last_row = triangle[-1]
            curr_row = []
            for j in range(i):
                curr_row.append(Solution.val(last_row, j - 1) + Solution.val(last_row, j))
            triangle.append(curr_row)
        return triangle

    @staticmethod
    def val(a, i):
        return a[i] if 0 <= i < len(a) else 0


if __name__ == "__main__":
    print Solution().generate(0)
    print Solution().generate(1)
    print Solution().generate(4)
    print Solution().generate(6)
    print Solution().generate(9)
    print Solution().generate(15)
