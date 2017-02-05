class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        keyboard_rows = [set(list("qwertyuiop")), set(list("asdfghjkl")), set(list("zxcvbnm"))]
        for word in words:
            word_chars = set(word.lower())
            for row in keyboard_rows:
                if word_chars.intersection(row) == word_chars:
                    result.append(word)
        return result


if __name__ == "__main__":
    print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
    print Solution().findWords([])
