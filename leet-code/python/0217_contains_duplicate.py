class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    ns = set()
    for num in nums:
      if num in ns:
        return False
      
      ns.add(num)
      
    return True