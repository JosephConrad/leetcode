class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combination([], range(1, 10), n, k)

    def combination(self, acc, candidates, n, k):
        if len(acc) == k:
            if sum(acc) == n:
                return [acc]
            else:
                return []
        result = []
        for i, elt in enumerate(candidates):
            result += self.combination(acc + [elt], candidates[i + 1:], n, k)
        return result


if __name__ == "__main__":
    print Solution().combinationSum3(3, 7)
    print Solution().combinationSum3(3, 9)
