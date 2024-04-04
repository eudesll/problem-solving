class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    m = {}
    for i in range(len(nums)):
      if nums[i] in m:
        return [m[nums[i]], i]
      
      m[target - nums[i]] = i
    
    return []