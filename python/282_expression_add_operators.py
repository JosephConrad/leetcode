class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        return self.sumToNumber(num, target, num[0], 1)

    def sumToNumber(self, num, target, exp, index):
        if index == len(num):
            value = self.eval(exp)
            return [exp] if value != "parse_error" and value == target else []
        result = []
        for op in ['+', '-', '*', '']:
            result += self.sumToNumber(num, target, exp + op + num[index], index + 1)
        return result

    def eval(self, exp):
        values, ops, i = [], [], 0

        while i < len(exp):
            if exp[i].isdigit():
                number = ""
                while i < len(exp) and exp[i].isdigit():
                    number += exp[i]
                    i += 1
                if str(number) != str(int(number)):
                    return "parse_error"
                values.append(int(number))
            elif exp[i] in {'+', '-', '*'}:
                while len(ops) > 0 and self.hasPresedence(exp[i], ops[-1]):
                    values.append(self.apply(ops.pop(), values.pop(), values.pop()))

                ops.append(exp[i])
                i += 1
            else:
                assert False

        while len(ops) > 0:
            values.append(self.apply(ops.pop(), values.pop(), values.pop()))

        return values.pop()

    def apply(self, op, a, b):
        if op == '+':
            return a + b
        if op == '-':
            return b - a
        if op == '*':
            return a * b

    def hasPresedence(self, op1, op2):
        if op1 == '*':
            return False
        return True



if __name__ == "__main__":
    # print Solution().eval("10-5")
    # print Solution().addOperators("123", 6)
    # print Solution().addOperators("232", 8)
    print Solution().addOperators("105", 5)
    print Solution().addOperators("00", 0)
    print Solution().addOperators("", 9191)
    print Solution().addOperators("2147483647", 2147483647)
    print Solution().addOperators("3456237490", 9191)
