from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not Counter(ransomNote) - Counter(magazine)


class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c = Counter(magazine)
        for elt in ransomNote:
            if c[elt] == 0:
                return False
            c[elt] -= 1
        return True


if __name__ == "__main__":
    print Solution().canConstruct("a", "b")
    print Solution().canConstruct("aa", "ab")
    print Solution().canConstruct("aa", "aab")
