class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        n = len(s)
        if n > 12:
            return result
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.allValid(i, j, k, n, s):
                        result.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:n])
        return result

    def allValid(self, i, j, k, n, s):
        return self.isValid(s[:i]) and self.isValid(s[i:j]) and self.isValid(s[j:k]) and self.isValid(s[k:n])

    def isValid(self, s):
        if len(s) == 0 or (s[0] == '0' and s != "0"):
            return False
        return int(s) < 256


if __name__ == "__main__":
    print Solution().restoreIpAddresses("11111111111111111111111111111111111111111111111111111111111111111111111111111")
    print Solution().restoreIpAddresses("25525511135")
