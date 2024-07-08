class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = []
        self.set = set()

    def popSmallest(self) -> int:
        if self.heap:
            val = heapq.heappop(self.heap)
            self.set.remove(val)
            return val
        
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)