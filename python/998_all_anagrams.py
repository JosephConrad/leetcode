class Solution(object):
    def allAnagrams(self, word):
        """
        :type word: List[char]
        :rtype: int
        """
        self.size = len(word)
        return set(self.anagrams(word, []))

    def anagrams(self, letters, acc):
        if len(acc) == self.size:
            return [''.join(acc)]
        result = []
        for i, c in enumerate(letters):
            result += self.anagrams(letters[:i] + letters[i + 1:], acc + [c])
        return result


if __name__ == "__main__":
    print Solution().allAnagrams("mama")
