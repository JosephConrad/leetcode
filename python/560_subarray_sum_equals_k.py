from collections import defaultdict


class Solution(object):
    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n, count = len(nums), 0
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix[j] - prefix[i] == k:
                    count += 1
        return count

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = defaultdict(int)
        count, prefix, map[0] = 0, 0, 1
        for elt in nums:
            prefix += elt
            if prefix - k in map:
                count += map[prefix - k]
            map[prefix] += 1
        return count


if __name__ == "__main__":
    print Solution().subarraySum(nums=[1, 1, 1], k=2)
