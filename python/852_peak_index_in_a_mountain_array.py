from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        maks, maks_index = A[0], 0
        for i, elt in enumerate(A):
            if elt > maks:
                maks = elt
                maks_index = i
        return maks_index
        

if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([0,2,1,0]))
    print(Solution().peakIndexInMountainArray([0,1,0]))
    