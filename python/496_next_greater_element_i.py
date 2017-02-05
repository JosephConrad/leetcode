class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n1, n2 = len(nums1), len(nums2)
        pos = dict(zip(nums2, range(n2)))
        result = []
        for i, elt in enumerate(nums1):
            for j in range(pos[elt], n2):
                if nums2[j] > elt:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)

        return result


if __name__ == "__main__":
    print Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
    print Solution().nextGreaterElement(nums1=[], nums2=[])
    print Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4])
