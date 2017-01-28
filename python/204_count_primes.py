class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in xrange(2, n):
            if i * i >= n:
                break
            if prime[i] is False:
                continue
            for j in xrange(i * i, n, i):
                prime[j] = False
        return sum(prime)


if __name__ == "__main__":
    print Solution().countPrimes(1500000)
    print Solution().countPrimes(7)
    print Solution().countPrimes(1)
    print Solution().countPrimes(2)
