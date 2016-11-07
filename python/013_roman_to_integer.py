class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            r = self.decode(s, i)
            if i == len(s) - 1 or r >= self.decode(s, i + 1):
                result += r
            else:
                result += self.decode(s, i + 1) - r
                i += 1
            i += 1
        return result

    def decode(self, s, r):
        decoder = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        return decoder[s[r]]


class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, n = 0, len(s)

        for i in range(n):
            if i > 0 and self.decode(s, i - 1) < self.decode(s, i):
                result += self.decode(s, i) - 2 * self.decode(s, i - 1)
            else:
                result += self.decode(s, i)

        return result

    def decode(self, s, r):
        decoder = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        return decoder[s[r]]


if __name__ == "__main__":
    print Solution().romanToInt("I")
    print Solution().romanToInt("V")
    print Solution2().romanToInt("I")
    print Solution2().romanToInt("V")
