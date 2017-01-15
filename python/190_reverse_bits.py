class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return ''.join(list(reversed(format(n, 'b').zfill(32))))


if __name__ == "__main__":
    print Solution().reverseBits(19)
    print Solution().reverseBits(2147483648)
    print Solution().reverseBits(0)
