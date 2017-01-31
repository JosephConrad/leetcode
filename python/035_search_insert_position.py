class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, elt in enumerate(nums):
            if target <= elt:
                return i
        return len(nums)


if __name__ == "__main__":
    print Solution().searchInsert([1], 0)
