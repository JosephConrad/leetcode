class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        l, r, maks = 0, n-1, 0
        while l <= r:
            s = (l + r) / 2
            maks = max(maks, min(n - s, citations[s]))
            if n - s < citations[s]:
                r = s - 1
            elif n - s > citations[s]:
                l = s + 1
            else:
                break
        return maks


if __name__ == "__main__":
    print Solution().hIndex([1, 2, 3, 22, 24, 26, 27])
    print Solution().hIndex([1, 2, 2, 2, 2, 2])
    print Solution().hIndex([])
    print Solution().hIndex([0])
