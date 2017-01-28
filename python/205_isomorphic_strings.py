class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping.keys():
                if mapping[s[i]] != t[i]:
                    return False
            elif t[i] in mapping.values():
                return False
            else:
                mapping[s[i]] = t[i]
        return True


if __name__ == "__main__":
    print Solution().isIsomorphic("egg", "add")
    print Solution().isIsomorphic("foo", "bar")
