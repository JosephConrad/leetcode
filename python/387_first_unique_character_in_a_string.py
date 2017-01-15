class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = dict()
        num = dict()
        for index, elt in enumerate(s):
            pos[elt] = min(pos.get(elt, 1000000), index)
            num[elt] = num.get(elt, 0) + 1
        minimum = 100000
        for k, _ in num.items():
            if num[k] == 1:
                minimum = min(minimum, pos[k])
        return minimum if minimum < 100000 else -1