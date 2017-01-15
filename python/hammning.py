class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        get_binary = lambda x: format(x, 'b').zfill(32)
        nums = map(get_binary, nums)
        ones = [0] * 32
        for num in nums:
            for i, bit in enumerate(num):
                if bit == '1':
                    ones[i] += 1
        part = map(lambda x: (n - x) * x,  ones)
        return reduce(lambda x, y: x+y, part)


if __name__ == "__main__":
    print Solution().totalHammingDistance([4, 14, 2])
    print Solution().totalHammingDistance([4, 14, 4])


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.insert(0, 1)
        result = []
        for i in range(1, len(nums)):
            elt = nums[i]
            if nums[abs(elt)] > 0:
                nums[abs(elt)] = - nums[abs(elt)]
            else:
                result.append(abs(elt))
        return result


if __name__ == "__main__":
    print Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    print Solution().findDuplicates([10, 2, 5, 10, 9, 1, 1, 4, 3, 7])
