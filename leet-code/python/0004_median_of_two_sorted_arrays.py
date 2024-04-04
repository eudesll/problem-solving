class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    res = []
    i = 0; j = 0
    while i < len(nums1) and j < len(nums2):
      if nums1[i] < nums2[j]:
        res.append(nums1[i])
        i += 1
      else:
        res.append(nums2[j])
        j += 1
        
    if i != len(nums1):
      res += nums1[i:]
    elif j != len(nums2):
      res += nums2[j:]
    
    if len(res) % 2 == 0:
      return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2
    
    return res[len(res) // 2]