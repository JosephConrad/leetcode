import random


# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        result = self.nums[:]
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)                        # generate j number that will be at i-th position
            result[i], result[j] = result[j], result[i]
        return result


class Solution2(object):
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))


if __name__ == "__main__":
    # Your Solution object will be instantiated and called as such:
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
