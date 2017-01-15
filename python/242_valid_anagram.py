class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        for elt in s:
            d[elt] = d.get(elt, 0) + 1
        for elt in t:
            d[elt] = d.get(elt, 0) - 1
        for _, v in d.items():
            if v != 0:
                return False
        return True
