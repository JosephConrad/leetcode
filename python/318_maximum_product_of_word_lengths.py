# could be done faster
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n, maks = len(words), 0
        lengths, words = map(len, words), map(set, words)
        for i in range(n):
            for j in range(i, n):
                maks = max(maks, lengths[i] * lengths[j] if words[i].intersection(words[j]) == set([]) else 0)
        return maks


if __name__ == "__main__":
    print Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print Solution().maxProduct([])
