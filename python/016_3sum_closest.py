class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        closest_sum = 1000000
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            a = nums[i]
            while j < k:
                b = nums[j]
                c = nums[k]
                current_sum = a + b + c
                if abs(current_sum - target) < abs(closest_sum):
                    closest_sum = current_sum - target
                if current_sum - target <= 0:
                    j += 1
                elif current_sum - target > 0:
                    k -= 1
        return closest_sum + target


if __name__ == "__main__":
    print Solution().threeSum([-4, -1, -1, 0, 1, 2], 5)
