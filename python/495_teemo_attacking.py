class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        overall, prev_end = 0, 0
        for timestamp in timeSeries:
            overall += duration - max(0, prev_end - timestamp)
            prev_end = timestamp + duration
        return overall


if __name__ == "__main__":
    print Solution().findPoisonedDuration([1, 4], 2)
    print Solution().findPoisonedDuration([1, 2], 2)
