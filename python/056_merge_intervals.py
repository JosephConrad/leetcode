# 56. Merge Intervals
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        result = []
        curr = Interval(intervals[0].start, intervals[0].end)
        for inter in intervals:
            if inter.start > curr.end:
                result.append([curr.start, curr.end])
                curr.start = inter.start
            curr.end = max(curr.end, inter.end)
        result.append([curr.start, curr.end])
        return result