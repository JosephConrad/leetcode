# simply need to make it another way


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        acc = []
        self.allperm(acc, len(nums), [], nums)
        return acc

    def allperm(self, acc, size, perm, nums):
        if len(perm) == size:
            if perm not in acc:
                acc.append(perm)
            return
        for i in range(len(nums)):
            self.allperm(acc, size, perm + [nums[i]], nums[:i] + nums[i + 1:])


if __name__ == "__main__":
    print Solution().permuteUnique([1, 1, 2])
    print Solution().permuteUnique([1, 1, 0, 0, 1, -1, -1, 1])
