class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    print Solution().arrayPairSum([1, 2, 4, 3])
