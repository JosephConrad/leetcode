from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = defaultdict(lambda: s.count(c))
        for i, elt in enumerate(s):
            if c[elt] == 1:
                return i
        return -1


if __name__ == "__main__":
    # Your Solution object will be instantiated and called as such:
    print Solution().firstUniqChar("leetcode")
    print Solution().firstUniqChar("loveleetcode")
    print Solution().firstUniqChar("aa")
    print Solution().firstUniqChar("")
