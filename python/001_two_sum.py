# 1. Two Sum   QuestionEditorial Solution  My Submissions

# Given an array of integers, return indices of the two numbers such
#   that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def two_sum(array, target):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == target:
                return [i, j]


two_sum([2, 7, 11, 15], 9)
