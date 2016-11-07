class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = strs[0]
        for i in range(1, len(strs)):
            result = self.longest(result, strs[i])
        return result

    def longest(self, s1, s2):
        i = 0
        while i < min(len(s1), len(s2)):
            if s1[i] != s2[i]:
                break
            i += 1
        return s1[:i]


if __name__ == "__main__":
    print Solution().longestCommonPrefix(["aa", "aaa"])
