class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word in {word.upper(), word.lower(), word.title()}


if __name__ == "__main__":
    print Solution().detectCapitalUse("UDS")
