class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set(tuple(entrance))
        to_visit = deque([[entrance]])
        while to_visit:
            path = to_visit.popleft()
            loc = path[-1]
            if (loc[0] == 0 or loc[0] == len(maze) - 1 or loc[1] == 0 or loc[1] == len(maze[0]) - 1) and loc != entrance:
                return len(path) - 1
            
            neighbors = [[0,1],[0,-1],[-1,0],[1,0]]
            for n in neighbors:
                x, y = loc[0]+n[0], loc[1]+n[1]
                if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] != "+" and (x,y) not in visited:
                    to_visit.append(path + [[x,y]])
                    visited.add((x,y))
        
        return -1