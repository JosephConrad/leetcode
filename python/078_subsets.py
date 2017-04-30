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


class Solution2(object):
    def subsets(self, nums, begin=0, acc=[]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if begin == len(nums):
            return [acc]
        return self.subsets(nums, begin + 1, acc) + self.subsets(nums, begin + 1, acc + [nums[begin]])


if __name__ == "__main__":
    print Solution().subsets([1, 2, 3])
