class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)
        overflow = 1
        i = n - 1
        while overflow and i >= 0:
            s = digits[i] + overflow
            overflow = s / 10
            digits[i] = s % 10
            i -= 1
        return digits if not overflow else [overflow] + digits


if __name__ == "__main__":
    print Solution().plusOne([9, 9, 9, 9])
