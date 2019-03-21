class Solution(object):
    def largestPerimeter1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        i, maks = 2, 0
        
        while i < len(A):
            a = A[i-2]
            b = A[i-1]
            c = A[i]
            if a + b > c:
                maks = max(maks, a+b+c)
            i += 1
        return maks
    
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort() 
        size = len(A)
        for i in range(size-1, 1, -1): 
            a, b, c = A[i-2], A[i-1], A[i] 
            if a + b > c:
                return a + b + c 
        return 0
        