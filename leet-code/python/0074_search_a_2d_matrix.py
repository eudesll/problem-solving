class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def getCoordinates(index: int, width: int) -> List[int]:
      x = index // width
      y = index - (width * x)
      return [x, y]
      
    start, end = 0, len(matrix) * len(matrix[0]) - 1
    while start <= end:
      i = (start + end) // 2
      x, y = getCoordinates(i, len(matrix[0]))

      if matrix[x][y] == target:
        return True

      if matrix[x][y] < target:
        start = i + 1
      else:
        end = i - 1
    
    return False