class MinHeap:
    
    def __init__(self):
        self.heap= []

    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)

    def pop(self) -> int:
        if len(self.heap) == 0:
            return -1

        return heapq.heappop(self.heap)

    def top(self) -> int:
        val = self.pop()
        
        if val != -1:
            self.push(val)

        return val

    def heapify(self, nums: List[int]) -> None:
        heapq.heapify(nums)
        self.heap = nums
        