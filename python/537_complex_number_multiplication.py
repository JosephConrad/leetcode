import re


class Solution(object):
    def complexNumberMultiply2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = map(lambda x: int(x[:-1]) if 'i' in x else int(x), a.split("+"))
        br, bi = map(lambda x: int(x[:-1]) if 'i' in x else int(x), b.split("+"))
        return str(ar * br - ai * bi) + '+' + str(ar * bi + br * ai) + 'i'

    def complexNumberMultiply1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = map(int, a[:-1].split("+"))
        br, bi = map(int, b[:-1].split("+"))
        return '%d+%di' % (ar * br - ai * bi, ar * bi + br * ai)

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai, br, bi = map(int, re.findall('-?\d+', a + b))
        return '%d+%di' % (ar * br - ai * bi, ar * bi + br * ai)


if __name__ == "__main__":
    print Solution().complexNumberMultiply("1+1i", "1+1i")
    print Solution().complexNumberMultiply("1+-1i", "1+-1i")
