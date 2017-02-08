class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        left, right, n = [nums[0]], [nums[-1]], len(nums)
        for i in range(1, n):
            left.append(left[i - 1] * nums[i])
            right.append(right[i - 1] * nums[n - i - 1])
        right.reverse()
        print left
        print right
        result = []
        for i in range(n):
            result.append(self.get(left, i - 1) * self.get(right, i + 1))
        return result

    def get(self, left, i):
        return left[i] if 0 <= i < len(left) else 1


if __name__ == "__main__":
    print Solution().productExceptSelf([1, 2, 3, 4])
    print Solution().productExceptSelf([])
    print Solution().productExceptSelf([0, 0])
