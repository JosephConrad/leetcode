from math import sqrt


class Solution2(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        tab = [False] * (n + 1)
        for i in range(1, n):
            j = i
            while j < n + 1:
                tab[j] = not tab[j]
                j += i
        if n > 0:
            tab[-1] = not tab[-1]
        return sum(tab)


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(sqrt(n))


if __name__ == "__main__":
    print Solution().bulbSwitch(0)
    print Solution().bulbSwitch(2)
    print Solution().bulbSwitch(1)
    print Solution().bulbSwitch(3)
    print Solution().bulbSwitch(10)
    print Solution().bulbSwitch(15)
    print Solution().bulbSwitch(24)
