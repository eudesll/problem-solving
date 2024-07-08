class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m1 = set(nums1)
        m2 = set(nums2)

        return [list(m1-m2), list(m2-m1)]