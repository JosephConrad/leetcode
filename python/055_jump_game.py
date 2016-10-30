# 55. Jump Game
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        reachable = nums[0]
        for i, jump in enumerate(nums):
            if reachable < i < n:
                return False
            reachable = max(reachable, i + jump)
        return True

if __name__ == "__main__":
    print Solution().canJump([2, 0])
