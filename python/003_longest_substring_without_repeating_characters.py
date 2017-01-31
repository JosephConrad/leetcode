class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        max_length, length, prev = 0, 0, 0
        used = set()
        for elt in s:
            if elt in used:
                max_length = max(max_length, length)
                while s[prev] != elt:
                    used.remove(s[prev])
                    length -= 1
                    prev += 1
                prev += 1
            else:
                used.add(elt)
                length += 1
        return max(max_length, length)


if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("bbbbbb")
    print Solution().lengthOfLongestSubstring("dvdf")
