class Solution:
  def sortColors(self, nums: List[int]) -> None:
    # Dutch National Flag algorithm
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
      if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
      elif nums[mid] == 1:
        mid += 1
      else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
                
    # numsM = defaultdict(int)
    # for n in nums:
    #   numsM[n] += 1
    
    # i, index = 0, 0
    # while i < len(nums):
    #   if numsM[index] == 0:
    #     index += 1
    #   else:
    #     nums[i] = index
    #     numsM[index] -= 1
    #     i += 1