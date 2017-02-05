class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        n = len(nums)
        max_index, max_value = max(enumerate(nums), key=lambda p: p[1])
        stack, result = [], [-1] * n

        i = (max_index + 1) % n
        while i != max_index:
            elt = nums[i]
            while len(stack) > 0 and nums[stack[-1]] < elt:
                result[stack.pop()] = elt
            stack.append(i)
            i = (i + 1) % n

        for index in stack:
            if nums[index] != max_value:
                result[index] = max_value

        return result


class Solution2(object):
    def nextGreaterElements(self, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        result = [-1] * n
        for i in range(n):
            j = (i + 1) % n
            while i != j:
                if nums[j] > nums[i]:
                    result[i] = nums[j]
                    break
                j = (j + 1) % n

        return result


if __name__ == "__main__":
    x = list(reversed(range(1, 11)))
    print Solution().nextGreaterElements([1, 2, 4, 3])
    print ""
    print list(reversed(range(1, 11)))
    print Solution().nextGreaterElements(x)
    print Solution().nextGreaterElements([])
    print Solution().nextGreaterElements([1, 1, 1, 1, 1])
