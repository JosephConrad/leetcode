class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.rstrip().split(" ")
        return len(words[-1]) if len(words) > 0 else 0


if __name__ == '__main__':
    print Solution().lengthOfLastWord("a ")