class MyHashSet:
  # Should use hashmap (dict)
  def __init__(self):
    self.hashset = set()

  def add(self, key: int) -> None:
    self.hashset.add(key)

  def remove(self, key: int) -> None:
    if key in self.hashset:
      self.hashset.remove(key)

  def contains(self, key: int) -> bool:
    return key in self.hashset