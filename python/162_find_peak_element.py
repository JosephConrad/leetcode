class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN = -10000000000
        nums = [MIN] + nums + [MIN]
        return self.findPeak(0, len(nums) - 1, nums)

    def findPeak(self, l, r, nums):
        s = (l + r) / 2
        if nums[s - 1] <= nums[s] >= nums[s + 1]:
            return s - 1
        elif nums[s - 1] > nums[s]:
            return self.findPeak(l, s - 1, nums)
        else:
            return self.findPeak(s + 1, r, nums)


if __name__ == "__main__":
    print Solution().findPeakElement([1, 2, 3, 1])
    print Solution().findPeakElement([1, 2, 3, 4])
    print Solution().findPeakElement([1, 2])
    print Solution().findPeakElement([3, 2, 1])
    print Solution().findPeakElement([1])
