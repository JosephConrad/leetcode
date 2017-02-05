class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return j + 1


if __name__ == "__main__":
    print Solution().removeElement([3,2,2,3], 3)

# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         i, j = 0, len(nums) - 1
#         while i < len(nums):
#             if nums[-1] == val:
#                 nums.pop()
#                 continue
#             elif nums[i] == val:
#                 nums[i], nums[-1] = nums[-1], nums[i]
#                 continue
#             i += 1
#         return i
#
#
# if __name__ == "__main__":
#     print Solution().removeElement([1],1)
