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

from typing import List

def two_sum_naive(array, target):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == target:
                return [i, j]

def two_sum(array, target):
    d = {}
    for i, elt in enumerate(array):
        d[elt] = i 
    for i, elt in enumerate(array):
        needed = target - elt  
        if needed in d and i != d[needed]:
            return [d[needed], i]

def twoSum_best(nums: List[int], target: int) -> List[int]:
                      
        mapping = {n: i for i, n in enumerate(nums)}
        
        for i, num in enumerate(nums):
            diff = mapping.get(target - num, False)
            
            if diff and diff != i:
                return [i, diff]


print( two_sum([2, 7, 11, 15], 9) )
print( two_sum_naive([2, 7, 11, 15], 9) )
print( twoSum_best([2, 7, 11, 15], 9) )

