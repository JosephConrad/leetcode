class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        overflow = 0
        for i in range(max(len(a), len(b))):
            s = self.val(a, len(a) - 1 - i) + self.val(b, len(b) - 1 - i) + overflow
            overflow = int(s >= 2)
            result = str(s % 2) + result
        return "1" + result if overflow else overflow

    def val(self, a, i):
        return int(a[i]) if i >= 0 else 0


if __name__ == '__main__':
    print Solution().addBinary('11', '1')