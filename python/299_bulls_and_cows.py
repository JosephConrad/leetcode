from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows, count = 0, 0, defaultdict(int)

        for s, g in zip(secret, guess):
            if s != g:
                count[s] += 1

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            elif g in count and count[g] > 0:
                cows += 1
                count[g] -= 1

        return str(bulls) + "A" + str(cows) + "B"


if __name__ == "__main__":
    print Solution().getHint("1807", "7810")
    print Solution().getHint("1", "1")
    print Solution().getHint("11", "10")
    print Solution().getHint("1234", "0111")
    print Solution().getHint("1122", "1222")
