class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    output = [[]]
    
    # Cascading - O(N * 2^N)    
    # for num in nums:
    #   output += [curr + [num] for curr in output]
    
    # Backtracking - O(N * 2^N)  
    def backtrack(first = 0, curr = []):
      if len(curr) == k:  
        output.append(curr[:])
        return
      for i in range(first, n):
        curr.append(nums[i])
        backtrack(i + 1, curr)
        curr.pop()
        
    n = len(nums)
    for k in range(1, n + 1):
        backtrack()
    
    # Lexicographic
    # for i in range(2**n, 2**(n + 1)):
    #   bitmask = bin(i)[3:]
    #   output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
      
    return output