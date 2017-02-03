class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i + 1
            k = n - 1
            a = nums[i]
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    result.append([a, b, c])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return result


if __name__ == "__main__":
    print Solution().threeSum([-4, -1, -1, 0, 1, 2])
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print Solution().threeSum([0, 0, 0, 0])
