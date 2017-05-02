# https://discuss.leetcode.com/topic/28833/short-python-bfs


class Solution(object):
    def isValid(self, s):
        ctr = 0
        for c in s:
            ctr += (c == '(') - (c == ')')
            if ctr < 0:
                return False
        return ctr == 0

    def removeInvalidParentheses(self, s):
        level = {s}
        while True:
            valid = filter(self.isValid, level)
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}


if __name__ == "__main__":
    print Solution().removeInvalidParentheses("(a)())()")
