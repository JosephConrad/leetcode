class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if str == "":
            return 0

        i = 0
        while i < len(str) and str[i] == " ":
            i += 1

        flag = -1 if str[i] == '-' else 1
        i = i+1 if str[i] == '-' or str[i] == '+' else i

        number = 0
        while i < len(str) and '9' >= str[i] >= '0':
            number = 10 * number + int(str[i])
            i += 1

        number *= flag

        if number > INT_MAX:
            number = INT_MAX

        if number < INT_MIN:
            number = INT_MIN

        return number


if __name__ == "__main__":
    # print Solution().myAtoi("23")
    print Solution().myAtoi(" b11228552307")
