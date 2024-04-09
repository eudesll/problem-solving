class Solution:
  def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    total = 0
    for i in range(len(tickets)):
      to_reduce = tickets[k] if i <= k else tickets[k] - 1
      total += min(tickets[i], to_reduce)
  
    return total