class Solution:
  def trap(self, height: List[int]) -> int:
    n = len(height)
    res = 0
    
    # Two Pointer - O(n) O(1)
    i, j = 0, len(height) - 1
    left_max, right_max = -1, -1
    
    while i < j:
      left_max = max(left_max, height[i])
      right_max = max(right_max, height[j])
      
      if left_max <= right_max:
        res += left_max - height[i]
        i += 1
      else:
        res += right_max - height[j]
        j -= 1
    
    return res
  
    # Monotonic Stack - O(n) O(n)
    stack = []
    for r in range(n):
      while stack and height[stack[-1]] < height[r]: # 0 < 2
        top = stack.pop() # 0
        
        if not stack:
          break
        
        l = stack[-1] # 1
        h = min(height[r] - height[top], height[l] - height[top]) # min(2 - 0, 1 - 0) == 1
        w = r - l - 1 # 3 - 1 - 1 == 1

        res += h * w # 1 * 1 == 1
        
      stack.append(r)
      
    return res
    
    # Brute force - PrefixSum and SuffixSum - O(n) O(n+n)
    left_max = [0] * n
    for i in range(1, n):
      left_max[i] = max(height[i - 1], left_max[i - 1])
      
    right_max = [0] * n
    for i in range(n - 2, -1, -1):
      right_max[i] = max(height[i + 1], right_max[i + 1])
      
    for i in range(n):
      max_water_level = min(left_max[i], right_max[i])
      res += max(0, max_water_level - height[i])
    
    return res