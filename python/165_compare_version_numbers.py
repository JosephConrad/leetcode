class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        for i in range(0, max(len(v1), len(v2))):
            sign = self.sign(self.val(v1, i) - self.val(v2, i))
            if sign is not 0:
                return sign
        return 0

    def sign(self, elt):
        if elt > 0:
            return 1
        elif elt < 0:
            return -1
        return 0

    def val(self, a, i):
        return a[i] if i < len(a) else 0


if __name__ == "__main__":
    print Solution().compareVersion("1.2", "13.37")
    print Solution().compareVersion("0", "1")
