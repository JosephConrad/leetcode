class Solution(object):
    def titleToNumber(self, s):
        result = 0
        for i, c in enumerate(reversed(s)):
            result += (ord(c) % 32) * pow(26, i)
        return result


class Solution2(object):
    def titleToNumber(self, s):
        result = 0
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) % 32
        return result

if __name__ == "__main__":
    print Solution().titleToNumber("A")
    print Solution2().titleToNumber("A")
    print Solution().titleToNumber("AF")
    print Solution2().titleToNumber("AF")
