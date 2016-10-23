# 53. Maximum Subarray
#
# Find the contiguous subarray within an array
#   (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        maks = -100000
        global_maks = maks
        for elt in nums:
            maks = max(elt + maks, elt)
            global_maks = max(global_maks, maks)
        return global_maks

if __name__ == "__main__":
    print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print Solution().maxSubArray([-2, -2, -4, -4, -100])