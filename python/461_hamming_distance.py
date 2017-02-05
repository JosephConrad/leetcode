class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum(map(int, list('{0:0b}'.format(x ^ y))))

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ham = 0
        xor = x ^ y
        while xor:
            xor &= xor - 1
            ham += 1
        return ham

    def hammingDistance3(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    print Solution().hammingDistance(1, 4)
    print Solution().hammingDistance2(1, 4)
    print Solution().hammingDistance3(1, 4)
