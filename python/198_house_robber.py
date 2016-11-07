# 198. House Robber
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        taken = [0] * n
        taken[0] = nums[0]
        not_taken = [0] * n
        for i in range(1, n):
            not_taken[i] = max(not_taken[i-1], taken[i-1])
            taken[i] = not_taken[i-1] + nums[i]
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(not_taken[-1], taken[-1])

if __name__ == "__main__":
    print Solution().rob([1, 3, 5, 7, 1, 9, 100])
    print Solution().rob([1])
    print Solution().rob([])
