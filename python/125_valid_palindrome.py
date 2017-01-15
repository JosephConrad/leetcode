import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W+', '', s).lower()
        return s == s[::-1]


if __name__ == "__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
    print Solution().isPalindrome("sdfsdfasd")
