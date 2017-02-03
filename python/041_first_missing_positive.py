class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        first_positive = 0
        for elt in nums:
            if elt > 0:
                first_positive = elt
                break
        if not first_positive:
            return 1

        for i in range(n):
            if nums[i] < 1:
                nums[i] = elt

        for i, elt in enumerate(nums):
            value = abs(elt)
            if value < n + 1:
                nums[value-1] = -abs(nums[value-1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1