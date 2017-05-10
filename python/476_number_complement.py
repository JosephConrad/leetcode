class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = '1' * len(bin(num)[2:])
        m = int(mask, 2)
        return m ^ num