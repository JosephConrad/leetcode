from collections import defaultdict


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2s, s2p = defaultdict(lambda: ""), defaultdict(lambda: "")

        str = str.split(" ")
        if len(pattern) != len(str):
            return False

        for p, s in zip(pattern, str):

            if p2s[p] == "":
                p2s[p] = s
            elif p2s[p] != s:
                return False

            if s2p[s] == "":
                s2p[s] = p
            elif s2p[s] != p:
                return False

        return True


if __name__ == "__main__":
    # print Solution().wordPattern(pattern="abba", str="dog cat cat dog")
    # print Solution().wordPattern(pattern="abba", str="dog dog dog dog")
    print Solution().wordPattern(pattern="abc", str="b c a")
    # print Solution().wordPattern(pattern="", str="")
