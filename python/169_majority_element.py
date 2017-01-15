class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = nums[0]
        cand_count = 1
        for i in range(1, len(nums)):
            elt = nums[i]
            if elt == cand:
                cand_count += 1
            else:
                cand_count -= 1
                if cand_count == 0:
                    cand = elt
                    cand_count = 1
        return cand


if __name__ == "__main__":
    print Solution().majorityElement([4, 5, 43, 452, 34, 34, 5, 234, 3, 3, 3, 3, 3, 3, 3, 3])
