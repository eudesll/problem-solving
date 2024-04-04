class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    # Kadane's Algorithm
    maxSum = -sys.maxsize - 1
    currentSum = 0
    
    for num in nums:
      currentSum = max(num, currentSum + num)
      maxSum = max(maxSum, currentSum)
        
    return maxSum