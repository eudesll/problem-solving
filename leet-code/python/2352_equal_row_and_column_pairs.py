class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rm = defaultdict(int)
        for r in grid:
            row = "_".join([str(x) for x in r])
            rm[row] += 1
        
        res = 0
        for i in range(len(grid)):
            column = []
            for j in range(len(grid)):
                column.append(str(grid[j][i]))

            c = "_".join(column)
            if c in rm:
                res += rm[c]
        
        return res