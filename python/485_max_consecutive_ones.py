class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maks_total = 0
        total = 0
        for elt in nums:
            total = total + 1 if elt == 1 else 0
            maks_total = max(maks_total, total)
        return maks_total


if __name__ == "__main__":
    print Solution().findMaxConsecutiveOnes([1, 1, 0, 1])
