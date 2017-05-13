# Good template for solving backtracking problems
#   https://discuss.leetcode.com/topic/79916/java-solution-backtracking/4


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.beautifulArrangement(1, [0], N)

    def beautifulArrangement(self, k, acc, N):
        if k == N + 1:
            return 1
        result = 0
        for i in range(1, N + 1):
            if i not in acc and (i % k == 0 or k % i == 0):
                result += self.beautifulArrangement(k + 1, acc + [i], N)
        return result


if __name__ == "__main__":
    print Solution().countArrangement(1)
    print Solution().countArrangement(2)
    print Solution().countArrangement(3)
    print Solution().countArrangement(4)
    print Solution().countArrangement(5)
