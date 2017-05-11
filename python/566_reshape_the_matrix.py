import itertools


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in xrange(r)]

if __name__ == "__main__":
    print Solution().matrixReshape(nums=[[1, 2], [3, 4]], r=2, c=4)
    print Solution().matrixReshape(nums=[[1, 2], [3, 4]], r=1, c=4)
