class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    distances = {}
    for point in points:
      d = pow(point[0], 2) + pow(point[1], 2)
      if d not in distances:
        distances[d] = []

      distances[d].append(point)
      
    distances_heap = list(distances.keys())
    heapq.heapify(distances_heap)
    
    res = []
    while len(res) < k:
      point = distances[heapq.heappop(distances_heap)]
      res += point
    
    return res