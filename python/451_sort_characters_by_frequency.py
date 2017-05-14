from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([k * v for k, v in Counter(s).most_common()])


class Solution1(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([k * v for k, v in sorted(Counter(s).iteritems(), key=lambda x: -x[1])])


class Solution2(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c, result = Counter(s), ""
        for k, v in sorted(c.iteritems(), key=lambda x: -x[1]):
            result += v * k
        return result


if __name__ == "__main__":
    print Solution().frequencySort("cccaaa")
    print Solution().frequencySort("loveleetcode")
