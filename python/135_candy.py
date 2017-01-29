import operator


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        return self.find_minima(candies, ratings)

    def find_minima(self, candies, ratings):
        candies[0] = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in reversed(xrange(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1
        return reduce(operator.add, candies)


if __name__ == "__main__":
    print Solution().candy([3, 2, 4, 7, 2, 1, 3, 8, 9, 0, 6, 2, 1])
    print Solution().candy([1, 2, 3, 2, 3, 5, 2, 5])
    print Solution().candy([2, 3, 2])
