class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.upper() or word == word.lower() or word == word.title()


if __name__ == "__main__":
    print Solution().detectCapitalUse("USA")
    print Solution().detectCapitalUse("USa")
    print Solution().detectCapitalUse("flaG")
    print Solution().detectCapitalUse("ads")
    print Solution().detectCapitalUse("Ads")
