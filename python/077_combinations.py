class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        return self.subset([], 1, n, k)

    def subset(self, acc, begin, n, k):
        if n - begin + 1 < k - len(acc):
            return []
        if len(acc) == k:
            return [acc]
        result = []
        for elt in range(begin, n + 1):
            result += self.subset(acc + [elt], max(elt + 1, begin + 1), n, k)
        return result


if __name__ == "__main__":
    print Solution().combine(20, 16)
