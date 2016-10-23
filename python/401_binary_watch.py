class Solution(object):
    def readBinaryWatch(self, num):
        return Solution.bin_watch(num, [], 0)

    @staticmethod
    def bin_watch(n, watch, k):
        result = []
        if len(watch) == n:
            Solution.format_watch(watch, result)
        for i in range(k, 10):
            result += Solution.bin_watch(n, watch + [i], i + 1)
        return result

    @staticmethod
    def format_watch(watch, result):
        hour, minute = 0, 0
        for lamp in watch:
            if lamp < 4:
                hour += pow(2, lamp)
            else:
                minute += pow(2, lamp - 4)
        if hour <= 11 and minute <= 59:
            result.append("%d:%02d" % (hour, minute))


if __name__ == "__main__":
    print Solution().readBinaryWatch(1)
    print Solution().readBinaryWatch(2)
