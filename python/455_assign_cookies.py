class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        result, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                result += 1
            j += 1
        return result


if __name__ == "__main__":
    print Solution().findContentChildren([1, 2, 3], [1, 1])
    print Solution().findContentChildren([1, 2, 3], [])
    print Solution().findContentChildren([], [1, 1])
    print Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8])
