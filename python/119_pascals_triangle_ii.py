class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        row = [1]
        for k in range(n):
            row.append(row[-1] * (n - k) / (k + 1))
        return row


if __name__ == "__main__":
    print Solution().getRow(0)
    print Solution().getRow(1)
    print Solution().getRow(2)
    print Solution().getRow(3)
    print Solution().getRow(4)
    print Solution().getRow(6)
    print Solution().getRow(9)
    print Solution().getRow(15)
