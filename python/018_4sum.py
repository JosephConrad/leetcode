class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            for j in range(i+1, n - 2):

                if nums[j] == nums[j-1] and j -i > 1:
                    continue
                k = j + 1
                l = n - 1
                a = nums[i]
                b = nums[j]
                # print str(i) + " " + str(j) + " " + str(k) + " " + str(l)
                while k < l:
                    c = nums[k]
                    d = nums[l]
                    if a + b + c + d < target:
                        k += 1
                    elif a + b + c + d > target:
                        l -= 1
                    else:
                        result.append([a, b, c, d])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l - 1] == nums[l]:
                            l -= 1
                        k += 1
                        l -= 1
        return result


if __name__ == "__main__":
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    print Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0)
    print Solution().fourSum([0,0,0,0], 0)
