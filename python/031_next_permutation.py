class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for k in range(n - 2, -2, -1):
            if k == -1 or nums[k] < nums[k + 1]:
                break

        if k >= -1:
            for l in range(n - 1, k, -1):
                if nums[l] > nums[k]:
                    nums[l], nums[k] = nums[k], nums[l]
                    break

        self.invert(k + 1, n - 1, nums)

    def invert(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    for perm in [[2, 3, 1], [1, 3, 2], [3, 2, 1], [1, 2, 3, 7, 8]]:
        Solution().nextPermutation(perm)
        print perm
