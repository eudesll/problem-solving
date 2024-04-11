class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    maxArea = 0
    
    def checkIslandArea(r, c):
      if r not in range(len(grid)) or c not in range(len(grid[r])) or grid[r][c] == 0:
        return 0
      
      grid[r][c] = 0
      count = 1
      for dr, dc in (1,0), (-1,0), (0,-1), (0,1):
        count += checkIslandArea(r + dr, c + dc)
      
      return count
      
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == 1:
          area = checkIslandArea(i, j)
          maxArea = max(maxArea, area)
    
    return maxArea