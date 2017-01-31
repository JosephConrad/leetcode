class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        for elt in path:
            if elt == "..":
                if len(stack) > 0:
                    stack.pop()
            elif elt == "." or elt == "":
                pass
            else:
                stack.append(elt)
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    print Solution().simplifyPath("/a/./b/../../c/")
    print Solution().simplifyPath("/home/")
