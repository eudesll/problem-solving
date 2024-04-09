import heapq

class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.k = k
    self.nums = nums
    self.heap = []
    
    for num in nums:
      self.addHeap(num)

  def add(self, val: int) -> int:
    self.nums.append(val)
    return self.addHeap(val)
    
  def addHeap(self, num: int) -> int:
    if len(self.heap) > self.k:
      heapq.heappush(self.heap, num)
    else:
      if self.heap[0] < num:
        heapq.heappushpop(self.heap, num)
    
    return self.heap[0]