class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

            elif nums[j] == 1:
                j += 1

            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1


if __name__ == "__main__":
    tab = [0, 1, 0, 2, 1]
    Solution().sortColors(tab)
    print tab
