class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combination([], candidates, target)

    def combination(self, acc, candidates, target):
        if sum(acc) > target:
            return []
        elif sum(acc) == target:
            return [acc]
        result = []
        for i, elt in enumerate(candidates):
            result += self.combination(acc + [elt], candidates[i:], target)
        return result


if __name__ == "__main__":
    print Solution().combinationSum([2, 3, 6, 7], 7)
