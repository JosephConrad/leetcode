class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        maks = 0
        nums.sort()
        pre = nums[0]
        for elt in nums:
            maks = max(maks, abs(pre-elt))
            pre = elt
        return maks


if __name__ == "__main__":
    print Solution().maximumGap([4, 3, 2, 7, 8, 2, 3, 1])
    print Solution().maximumGap([10, 2, 5, 10, 9, 1, 1, 4, 3, 7])
    print Solution().maximumGap([4, 7, 1, 9, 0, 3])
    print Solution().maximumGap([1,10,100])
