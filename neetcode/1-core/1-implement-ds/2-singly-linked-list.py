class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head is None:
          return -1

        i = 0
        current = self.head
        while i < index:
          if current['next'] is None:
              return -1

          current = current['next']
          i += 1

        return current['val']

    def insertHead(self, val: int) -> None:
        self.head = {'val': val, 'next': self.head}

    def insertTail(self, val: int) -> None:
        if self.head is None:
          self.insertHead(val)
          return

        current = self.head
        while current['next'] is not None:
          current = current['next']
        current['next'] = {'val': val, 'next': None}

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
          self.head = self.head['next']
          return True

        i = 0
        current = self.head
        while current is not None and i+1 != index:
          i += 1
          current = current['next']

        if current is None or current['next'] is None:
          return False

        current['next'] = current['next']['next']        
        return True

    def getValues(self) -> List[int]:
        values = []

        current = self.head
        while current is not None:
          values.append(current['val'])
          current = current['next']

        return values