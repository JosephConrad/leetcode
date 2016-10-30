class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenths = {u')': u'(', u'}': u'{', u']': u'['}
        for p in s:
            if p in parenths.values():
                stack.append(p)
            elif len(stack) > 0 and parenths[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    print Solution().isValid("()")
    print Solution().isValid("([])")
    print Solution().isValid("()[]")
    print Solution().isValid("())")
