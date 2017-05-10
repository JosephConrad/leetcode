class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) / 2, len(set(candies)))


if __name__ == "__main__":
    print Solution().distributeCandies(candies=[1, 1, 2, 3])
    print Solution().distributeCandies(candies=[1, 1, 2, 2, 3, 3])
