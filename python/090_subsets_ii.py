class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        acc = []
        self.sub([], 0, sorted(nums), acc)
        return acc

    def sub(self, acc, begin, nums, result):
        if begin == len(nums):
            if acc not in result:
                return result.append(acc)
            return
        self.sub(acc, begin + 1, nums, result)
        self.sub(acc + [nums[begin]], begin + 1, nums, result)


if __name__ == "__main__":
    print Solution().subsetsWithDup([1, 2, 2])
