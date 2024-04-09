from collections import OrderedDict

class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.dic = OrderedDict()

  def get(self, key: int) -> int:
    if key not in self.dic:
        return -1
    self.dic.move_to_end(key)
    return self.dic[key]

  def put(self, key: int, value: int) -> None:
    if key in self.dic:
      self.dic[key] = value
      self.dic.move_to_end(key)
    else:
      self.dic[key] = value
      if len(self.dic) > self.capacity:
        self.dic.popitem(False)