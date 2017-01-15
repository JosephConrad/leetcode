class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited and n != 1:
            visited.add(n)
            digits = [int(x) for x in str(n)]
            n = sum(map(lambda a: pow(a, 2), digits))
        if n == 1:
            return True
        return False


if __name__ == "__main__":
    print Solution().isHappy(19)
    print Solution().isHappy(0)

