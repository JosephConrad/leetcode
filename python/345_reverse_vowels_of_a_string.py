class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels, tab = "aeiouAEIOU", list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if tab[i] in vowels and tab[j] in vowels:
                tab[i], tab[j] = tab[j], tab[i]
                i += 1
                j -= 1
            if tab[i] not in vowels:
                i += 1
            if tab[j] not in vowels:
                j -= 1
        return ''.join(tab)


if __name__ == "__main__":
    print Solution().reverseVowels("leetcode")
