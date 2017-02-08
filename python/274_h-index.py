class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        maks = 0
        citations.sort(reverse=True)
        for i, citation in enumerate(citations):
            maks = max(maks, min(citation, i + 1))
        return maks

if __name__ == "__main__":
    print Solution().hIndex([3, 0, 6, 1, 5])
    print Solution().hIndex([1, 2, 2, 2, 2, 2])
    print Solution().hIndex([6, 2, 2, 2, 2, 2])
    print Solution().hIndex([])