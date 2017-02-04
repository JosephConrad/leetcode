class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while i + j >= 0 and j >= 0 and i >= 0:
            if nums1[i] < nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1

        while j >= 0:
            nums1[i + j + 1] = nums2[j]
            j -= 1

if __name__ == "__main__":
    a1 = [1, 2, 3, 4, 5, 0]
    a2 = [6]
    Solution().merge(a1, 5, a2, 1)
    print a1
