class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        return "{}/({})".format(nums[0], '/'.join(nums[1:])) if len(nums) >= 3 else '/'.join(nums)

    def optimalDivision1(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        div = '/'.join(map(str, nums))
        return "%s(%s)" % (div[0:div.find('/') + 1], div[div.find('/') + 1:]) if len(nums) >= 3 else div


if __name__ == "__main__":
    print Solution().optimalDivision([1000, 100, 10, 2])
