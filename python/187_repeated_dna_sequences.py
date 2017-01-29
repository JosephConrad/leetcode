class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strings = dict()
        for i in range(10, len(s)+1):
            elt = s[i - 10:i]
            strings[elt] = strings.get(elt, 0) + 1
        return [k for k, v in strings.iteritems() if v > 1]


if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
