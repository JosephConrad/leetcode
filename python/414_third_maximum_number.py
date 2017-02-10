class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = maks = max(nums)
        for i in range(0, 2):
            nums = filter(lambda x: x != maks, nums)
            maks = max(nums) if nums else global_max
        return maks


if __name__ == "__main__":
    print Solution().thirdMax([1, 2])
