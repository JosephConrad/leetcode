def positionToNumber(x):
    return str(x[0] * 3 + x[1] + 1 if x[0] < 3 else 0)


def toNumber(positions):
    return ''.join(map(positionToNumber, positions))


class Solution(object):
    def __init__(self):
        self.validPoints = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 1)]
        self.moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (1, -2), (2, -1), (-2, -1), (-1, -2)]

    def generate(self, length, nums):
        if nums[-1] not in self.validPoints:
            return []
        if len(nums) == length:
            return [nums]
        result = []
        for dx, dy in self.moves:
            x, y = nums[-1][0], nums[-1][1]
            result += self.generate(length, nums + [(x + dx, y + dy)])
        return result

    def validNumbers(self, length):
        result = []
        for x, y in self.validPoints:
            result += map(toNumber, self.generate(length, [(x, y)]))
        return result


if __name__ == "__main__":
    print Solution().validNumbers(length=1)
    print Solution().validNumbers(length=2)
    print Solution().validNumbers(length=10)
