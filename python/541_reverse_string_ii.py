class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k) if s else ""


if __name__ == "__main__":
    print Solution().reverseStr(s="abcdefg", k=2)
