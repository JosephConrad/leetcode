class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0
        for elt in nums:
            if nums[last] != elt:
                last += 1
                nums[last] = elt
        return last + 1


if __name__ == "__main__":
    print Solution().removeDuplicates([1, 2, 3, 7, 7, 24, 24, 25])
