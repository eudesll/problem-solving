class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    k = r
    while l <= r:
      m = (l + r) // 2
      total = 0
      
      for pile in piles:
        total += math.ceil(pile / m)
        if total > h:
          break
      
      if total > h:
        l = m + 1
      else:
        r = m - 1
        k = min(k, m)

    return k