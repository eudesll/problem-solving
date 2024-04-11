class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    fresh = 0
    rotten = deque()
    for r in range(len(grid)):
      for c in range(len(grid[r])):
        if grid[r][c] == 1:
          fresh += 1
        elif grid[r][c] == 2:
          rotten.append((r, c))
          
    spread_time = 0
    while rotten:
      for _ in range(len(rotten)):
        r, c = rotten.popleft()
        ns = [(0, -1),(-1, 0),(0, 1),(1, 0)]
        for dr, dc in ns:
          dr += r
          dc += c
          if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[dr]) and grid[dr][dc] == 1:
            rotten.append((dr, dc))
            grid[dr][dc] = 2
            fresh -= 1
      
      if rotten:
        spread_time += 1
    
    if fresh > 0:
      return -1
    
    return spread_time