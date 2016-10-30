class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0, 1]
        while len(bits) <= num:
            bits += map(lambda num: num + 1, bits)
        return bits[:num + 1]


if __name__ == "__main__":
    print Solution().countBits(5)
    print Solution().countBits(10)
