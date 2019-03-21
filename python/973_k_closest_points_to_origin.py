class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """ 
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[0:K]