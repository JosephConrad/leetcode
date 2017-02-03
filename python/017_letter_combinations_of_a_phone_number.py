class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup, codes = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], [""]
        for digit in digits:
            new_codes = []
            for code in codes:
                for letter in lookup[int(digit)]:
                    new_codes.append(code + letter)
            codes = new_codes
        return codes if len(digits) > 0 else []


if __name__ == "__main__":
    print Solution().letterCombinations("23")
