class TreeMap:
    
    def __init__(self):
      self.root = None

    def insert(self, key: int, val: int) -> None:
      if self.root is None:
        self.root = {'key': key, 'val': val, 'left': None, 'right': None}
        return

      current = self.root
      while True:
        if key < current['key']:
          if current['left'] is None:
            current['left'] = {'key': key, 'val': val, 'left': None, 'right': None}
            return
          current = current['left']
        elif key > current['key']:
          if current['right'] is None:
            current['right'] = {'key': key, 'val': val, 'left': None, 'right': None}
            return
          current = current['right']
        else:
          current['val'] = val
          return

    def get(self, key: int) -> int:
      if self.root is None:
        return -1
      
      current = self.root
      while current is not None:
        if key < current['key']:
          current = current['left']
        elif key > current['key']:
          current = current['right']
        else:
          return current['val']
      
      return -1

    def getMin(self) -> int:
      if self.root is None:
        return -1

      current = self.root
      while current['left'] is not None:
        current = current['left']
      
      return current['val']


    def getMax(self) -> int:
      if self.root is None:
        return -1

      current = self.root
      while current['right'] is not None:
        current = current['right']
      
      return current['val']


    def remove(self, key: int) -> None:
      if self.root is None:
        return

      parent = None
      current = self.root
      while current is not None:
        if key < current['key']:
          current = current['left']
        elif key > current['key']:
          current = current['right']
        else:
          break
        parent = current
      
      if parent is None:
        if current['left'] is None and current['right'] is None:
          self.root = None
        elif current['left'] is None:
          self.root = current['right']
        elif current['right'] is None:
          self.root = current['left']
        else:
          successor_parent = current
          successor = current['right']
          while successor['left'] is not None:
            successor_parent = successor
            successor = successor['left']

          current['key'] = successor['key']
          current['val'] = successor['val']
          current['right'] = successor['right']
          successor = None

    def getInorderKeys(self) -> List[int]:
      return self.inorderKeys(self.root, [])

    def inorderKeys(self, node, res: List[int]) -> List[int]:
      if node is None:
        return res

      res = self.inorderKeys(node['left'], res)
      res.append(node['key'])
      res = self.inorderKeys(node['right'], res)
      return res