class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            a = numbers[i]
            b = numbers[j]
            if a + b == target:
                return [i + 1, j + 1]
            elif a + b < target:
                i += 1
            else:
                j -= 1


if __name__ == "__main__":
    print Solution().twoSum(numbers=[2, 7, 11, 15], target=9)
