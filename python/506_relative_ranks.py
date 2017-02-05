class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        results = [0] * n
        ranks = zip(nums, range(n))
        ranks.sort(key=lambda t: t[0], reverse=True)
        for i, rank in enumerate(ranks):
            if i == 0:
                results[rank[1]] = "Gold Medal"
            elif i == 1:
                results[rank[1]] = "Silver Medal"
            elif i == 2:
                results[rank[1]] = "Bronze Medal"
            else:
                results[rank[1]] = str(i + 1)
        return results


if __name__ == "__main__":
    print Solution().findRelativeRanks([8, 6, 3, 10, 1])
    print Solution().findRelativeRanks([])
