import operator


# 137. Single Number  ii
#
# Given an array of integers, every element appears three times except for one.
#   Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it
#   without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)


class Solution2(object):
    def singleNumber(self, nums):
        result = 0
        for i in range(32):
            bit_num = Solution.calc_bits_num(nums, i)
            result |= bit_num << i
        return result

    @staticmethod
    def calc_bits_num(nums, i):
        bit_sum = 0
        for num in nums:
            bit_sum += num >> i & 1
        bit_sum %= 3
        return bit_sum


class Solution3(object):
    def singleNumber(self, nums):
        freq = dict()
        for elt in nums:
            value = freq.get(elt, 0)
            freq[elt] = value + 1
        for key, value in freq.iteritems():
            if value is not 3:
                return key


if __name__ == "__main__":
    print Solution().singleNumber([3, 3, 4, 5, 5, 8, 5, 4, 4, 3])
