# Time O(n)
# Space O(log n)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        binaryCounter = 0
        for n in nums:
            if 1 << n & binaryCounter != 0:
                return n
            binaryCounter |= 1 << n


if __name__ == "__main__":
    print Solution().findDuplicate([1, 2, 3, 4, 6, 5, 8, 3, 7])
