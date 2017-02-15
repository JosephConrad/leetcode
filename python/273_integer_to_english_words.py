singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
         "nineteen"]
dozens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"

        units, result = ["Billion", "Million", "Thousand", ""], []
        num, n = str(num), len(num)

        while n > 0:
            n -= 3
            unit = units.pop()
            result = self.three_digits(num[max(0, n):n + 3], unit) + result

        return ' '.join(filter(lambda x: x != "", map(lambda x: x.title(), result)))

    def three_digits(self, num, unit):
        num = str(int(num))
        st = int(num[0])
        if int(num) == 0:
            return []
        if int(num) >= 100:
            result = [singles[st], "hundred"] + self.three_digits(num[1:], "")
        elif int(num) >= 20:
            result = [dozens[st]] + self.three_digits(num[1], "")
        elif int(num) >= 10:
            result = [teens[int(num[-1])]]
        else:
            result = [singles[int(num)]]
        return result + [unit]


if __name__ == "__main__":
    print Solution().numberToWords(323212)
    print Solution().numberToWords(3232128123)
    print Solution().numberToWords(123)
    print Solution().numberToWords(813)
    print Solution().numberToWords(802)
    print Solution().numberToWords(02)
    print Solution().numberToWords(800)
    print Solution().numberToWords(50868)
    print Solution().numberToWords(1099)
    print Solution().numberToWords(1000000)
