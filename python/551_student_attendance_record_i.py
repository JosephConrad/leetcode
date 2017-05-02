class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # return not re.search('A.*A|LLL', s)
        return not (s.count('A') > 1 or 'LLL' in s)
