class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums) ^ reduce(lambda x, y: x ^ y, range(len(nums) + 1))


if __name__ == "__main__":
    print Solution().missingNumber([0, 1, 3])