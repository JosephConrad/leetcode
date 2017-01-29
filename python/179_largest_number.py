class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums_str = map(str, nums)
        nums_str.sort(Solution.comparator)
        # str -> int and back int -> str to handle result like "000"
        return str(int(''.join(reversed(nums_str))))

    @staticmethod
    def comparator(x, y):
        return int(x + y) - int(y + x)


if __name__ == "__main__":
    print Solution().largestNumber([3, 30, 9, 34, 5])
    print Solution().largestNumber([2, 1])
    print Solution().largestNumber([0, 0])
