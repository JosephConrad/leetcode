class Solution(object):
    def countAndSay(self, n):
        seq = "1"
        for i in xrange(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, result = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i+1]:
                cnt += 1
                i += 1
            result += str(cnt) + seq[i]
            i += 1
        return result


if __name__ == "__main__":
    for i in range(1, 10):
        print Solution().countAndSay(i)