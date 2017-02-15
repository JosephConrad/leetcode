class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b = 0, 0
        # otrzymujemy tutaja x xor y
        for n in nums:
            a ^= n
        # robimy xora, aby otrzymac bit na ktorym sie nasze rozne liczby sie roznia
        xor = a & -a
        # dalej rozwiazujemy zadanie, ze wszystkie liczby sa podwojne w tablicy, a tylko jedna jest pojedyncza
        a = 0
        for n in nums:
            if xor & n:
                a ^= n
            else:
                b ^= n
        return [a, b]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b = 0, 0
        for n in nums:
            a ^= n
        for n in nums:
            if a & -a & n:
                b ^= n
        return [a ^ b, b]


if __name__ == "__main__":
    print Solution().singleNumber([2, 2, 1, 5, 3, 3])
    print Solution().singleNumber([1, 2, 1, 3, 2, 5])
