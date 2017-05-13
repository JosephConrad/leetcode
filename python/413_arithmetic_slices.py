class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n, result = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                n += 3 if n == 0 else 1
                result += n - 2
            else:
                n = 0
        return result


if __name__ == "__main__":
    print Solution().numberOfArithmeticSlices(A=[1, 2, 3, 4])
    print Solution().numberOfArithmeticSlices(A=[1, 1, 2, 5, 7])
