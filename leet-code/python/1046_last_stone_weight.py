class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    n_stones = [-s for s in stones]
    heapq.heapify(n_stones)
    
    while len(n_stones) > 1:
      heapq.heappush(n_stones, heapq.heappop(n_stones) - heapq.heappop(n_stones))
    
    return n_stones[0] * -1