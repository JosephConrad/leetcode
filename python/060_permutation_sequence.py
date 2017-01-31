class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        acc = self.allperm(n, [], list(range(1, n+1)), k)
        return ''.join(map(str, acc[k-1]))

    def allperm(self, size, perm, nums, k):
        if len(perm) == size:
            return [perm]
        result = []
        for i in range(len(nums)):
            result += self.allperm(size, perm + [nums[i]], nums[:i] + nums[i + 1:])
            if len(result) > k:
                return result
        return result


if __name__ == "__main__":
    print Solution().getPermutation(3, 4)
