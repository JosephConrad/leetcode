import bisect
    
class Solution(object):
    def sortedSquaresBasic(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([elt**2 for elt in A]) 

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """ 
        result = []
        split = bisect.bisect_right(A,0)
        pow2 = lambda elt: elt**2
        neg = [ pow2(elt) for elt in reversed(A[:split]) ]
        pos = [ pow2(elt) for elt in A[split:] ]
        
        i,j = 0, 0
        while i < len(neg) and j < len(pos):
            if abs(neg[i]) < abs(pos[j]):   
                result.append(neg[i])
                i += 1
            else: 
                result.append(pos[j])
                j += 1
        result += neg[i:]
        result += pos[j:]
        return result  

    def sortedSquares2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """ 
        result = []
        split = bisect.bisect_right(A,0)
        A = [ a**2 for a in A ]
        neg = A[:split][::-1]
        pos = A[split:]
        
        i,j = 0, 0
        while i < len(neg) and j < len(pos):
            if abs(neg[i]) < abs(pos[j]):   
                result.append(neg[i])
                i += 1
            else: 
                result.append(pos[j])
                j += 1
        result += neg[i:]
        result += pos[j:]
        return result
        