class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, local_max, local_min = float("-inf"), 1, 1
        for num in nums:
            local_max, local_min = max(num, local_max * num, local_min * num), min(num, local_max * num, local_min * num)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == "__main__":
    print Solution().maxProduct([2, 3, -2, 4])
    print Solution().maxProduct([2, 3, 0, -2, 4, -4, 0, 4])
    print Solution().maxProduct([-2])
