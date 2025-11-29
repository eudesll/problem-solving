class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c + 1]
                self.sum_matrix[r + 1][c + 1] = prefix + above
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1 - 1][col2]
        left = self.sum_matrix[row2][col1 - 1]
        topLeft = self.sum_matrix[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft

""" ONE-DIMENSIONAL PREFIX SUM
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.num_cols = len(matrix[0])
        self.p = [0]
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                previous = self.p[self.coordToIndex(i, j)]
                self.p.append(previous + c)

    def coordToIndex(self, row, col):
        return row * self.num_cols + col

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        area_sum = 0
        for i in range(row1, row2 + 1):
            area_sum += self.p[self.coordToIndex(i, col2) + 1] - self.p[self.coordToIndex(i, col1)]
        
        return area_sum
"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)