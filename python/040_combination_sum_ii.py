class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combination([], sorted(candidates), target)

    def combination(self, acc, candidates, target):
        if sum(acc) > target:
            return []
        elif sum(acc) == target:
            return [acc]
        result = []
        generated = set()
        for i, elt in enumerate(candidates):
            if elt not in generated:
                result += self.combination(acc + [elt], candidates[i + 1:], target)
            generated.add(elt)
        return result


if __name__ == "__main__":
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
