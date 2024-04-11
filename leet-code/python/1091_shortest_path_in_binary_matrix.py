from collections import deque

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] == 1:
      return -1
    
    dq = deque()
    r, c = 0, 0
    visited = set()
    
    dq.append((r, c))
    visited.add((r, c))
    
    length = 1
    while dq:
      for _ in range(len(dq)):
        r, c = dq.popleft()
        if r == len(grid) - 1 and c == len(grid) - 1:
            return length
          
        ns = [(-1, -1),(-1, 1),(1, 1),(1, -1), (0, -1),(-1, 0),(0, 1),(1, 0)]
        for dr, dc in ns:
          dr += r
          dc += c
          if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid) and (dr, dc) not in visited and grid[dr][dc] != 1:
            dq.append((dr, dc))
            visited.add((dr, dc))
      
      length += 1
    
    return -1
      
    