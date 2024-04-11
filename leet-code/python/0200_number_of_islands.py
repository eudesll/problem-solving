class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    res = 0
    
    def findBorders(r, c):
      if r not in range(len(grid)) or c not in range(len(grid[r])) or grid[r][c] == "0":
        return
      
      grid[r][c] = "0"
      for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
        findBorders(r + dr, c + dc)
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == "1":
          findBorders(i, j)
          res += 1
    
    return res