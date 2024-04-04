class HashTable:
    
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.size = 0
      self.dict = {}

    def insert(self, key: int, value: int) -> None:
      self.dict[key] = value
      self.size += 1

      if self.size >= self.capacity / 2:
        self.resize()

    def get(self, key: int) -> int:
      if key not in self.dict:
        return -1

      return self.dict[key]

    def remove(self, key: int) -> bool:
      if key not in self.dict:
        return False

      del self.dict[key]
      self.size -= 1
      return True

    def getSize(self) -> int:
      return self.size

    def getCapacity(self) -> int:
      return self.capacity

    def resize(self) -> None:
      self.capacity *= 2

a = HashTable(4)
a.insert(1, 2)
a.get(1)
a.insert(1,3)
a.get(1)
a.insert(2,4)
a.remove(1)
a.get(1)