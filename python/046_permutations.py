class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.allperm(len(nums), [], nums)

    def allperm(self, size, perm, nums):
        if len(perm) == size:
            return [perm]
        result = []
        for n in nums:
            result += self.allperm(size, perm + [n], list(set(nums) - set([n])))
        return result


if __name__ == "__main__":
    print Solution().permute([1, 2, 3])
