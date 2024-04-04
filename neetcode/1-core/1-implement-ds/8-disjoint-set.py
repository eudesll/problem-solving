class UnionFind:
    
    def __init__(self, n: int):
        self.arr = [-1] * n
        for i in range(n):
            self.arr[i] = i

    def find(self, x: int) -> int:
        if self.arr[x] == x:
            return x
        
        return self.find(self.arr[x])

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        xp = self.find(x)
        yp = self.find(y)

        if xp == yp:
            return False
        
        self.arr[yp] = xp
        return True

    def getNumComponents(self) -> int:
        comp = {}
        for i in range(len(self.arr)):
            p = self.find(self.arr[i])
            comp[p] = 1

        return len(comp)

