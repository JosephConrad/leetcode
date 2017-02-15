class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = zip(nums, range(len(nums)))
        l.sort(key=lambda t: t[0])
        for i in range(1, len(nums)):
            if l[i][0] == l[i - 1][0] and abs(l[i][1] - l[i - 1][1]) <= k:
                return True
        return False


if __name__ == "__main__":
    print Solution().containsNearbyDuplicate([2, 1], 2)
