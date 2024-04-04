from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      # - Sort in place using [:]
      nums[:] = sorted(set(nums))
      return len(nums)

      # - Two-pointers
      slow, fast = 0, 1
      while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
          fast += 1
        else:
          nums[slow+1] = nums[fast]
          fast += 1
          slow += 1

      return slow + 1

      # - Two-pointers - Simplified
      j = 0
      for i in range(1, len(nums)):
        if nums[j] != nums[i]:
          j += 1
        nums[j] = nums[i]
        
      return j + 1

      # - Using .pop()
      i = 1
      while i < len(nums):
        if nums[i] == nums[i - 1]:
          nums.pop(i)
        else:
          i += 1
      return len(nums)