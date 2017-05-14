from math import sqrt


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(sqrt(area)), 0, -1):
            if area % i == 0:
                return [area / i, i]


if __name__ == "__main__":
    print Solution().constructRectangle(4)
    print Solution().constructRectangle(5)
