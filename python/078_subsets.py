class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.sub([], 0, nums)

    def sub(self, acc, begin, nums):
        if begin == len(nums):
            return [acc]
        return self.sub(acc, begin + 1, nums) + self.sub(acc + [nums[begin]], begin + 1, nums)


if __name__ == "__main__":
    print Solution().subsets([1, 2, 3])
