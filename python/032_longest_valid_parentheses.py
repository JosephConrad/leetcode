class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, result = [], 0
        stack.append(-1)
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            elif p == ')':
                stack.pop()
                if len(stack) != 0:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        return result


if __name__ == "__main__":
    print Solution().longestValidParentheses("()()")
    print Solution().longestValidParentheses("(()(((()")
    print Solution().longestValidParentheses(")()())")
