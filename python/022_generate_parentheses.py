class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.generate(n, 0, [])

    def generate(self, n, balance, expression):
        acc = []
        if balance < 0 or balance > n or 2 * n < len(expression):
            return acc
        if len(expression) == 2 * n and balance == 0:
            acc += [''.join(expression)]
        acc += self.generate(n, balance + 1, expression + ['('])
        acc += self.generate(n, balance - 1, expression + [')'])
        return acc


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))
