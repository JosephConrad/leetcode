import operator


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        values, ops, i = [], [], 0
        for token in tokens:
            values.append(int(token) if token not in {'+', '-', '*', '/'} else self.apply(token, values.pop(), values.pop()))
        return values.pop()

    def apply(self, op, a, b):
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda x, y: int(float(x) / y)}
        return operators[op](b, a)


if __name__ == "__main__":
    print Solution().evalRPN(["2", "1", "+", "3", "*"])
    print Solution().evalRPN(["4", "13", "5", "/", "+"])
    print Solution().evalRPN(["3", "-4", "+"])
    print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
