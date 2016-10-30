from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for string in strs:
            groups[''.join(sorted(string))].append(string)
        return groups.values()


if __name__ == "__main__":
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
