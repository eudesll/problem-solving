class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    def dp(rows, cols):
      prev_row = [0] * cols
      
      for _ in range(rows - 1, -1, -1):
        curr_row = [0] * cols
        curr_row[-1] = 1
        
        for c in range(c - 2, -1, -1):
          curr_row[c] = curr_row[c + 1]
        
        prev_row = curr_row
      return prev_row[0]
    
    return dp(m, n)
    
    def memoization(r, c):
      if r >= m or c >= n:
        return 0
      
      if cache[r][c] > 0:
        return cache[r][c]
      
      if r == m-1 and c == n-1:
        return 1
      
      cache[r][c] = memoization(r, c + 1) + memoization(r + 1, c)
      return cache[r][c]
    
    cache = [[0] * n for i in range(m)]
    return memoization(0, 0)
  
    def brute_force(r, c):
      if r >= m or c >= n:
        return 0
      
      if r == m-1 and c == n-1:
        return 1
      
      return brute_force(r, c + 1) + brute_force(r + 1, c)
    
    return brute_force(0,0)