class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    # - Sorting
    # nums.sort()
    # n = len(nums)
    # return nums[n//2]
    
    # - HashMap
    digSum = {}
    for n in nums:
      if n not in digSum:
        digSum[n] = 0
      digSum[n] += 1
    
    bigNum = -1
    for n in digSum:
      if bigNum == -1 or digSum[n] > digSum[bigNum]:
        bigNum = n
    
    return bigNum

    # - Moore Voting Algorithm
    # count = 0
    # candidate = 0
    
    # for num in nums:
    #   if count == 0:
    #     candidate = num
      
    #   if num == candidate:
    #     count += 1
    #   else:
    #     count -= 1
    
    # return candidate