class ListNode:
  def __init__(self, val=0, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next
        
class MyLinkedList:

  def __init__(self):
    self.head = None
    self.size = 0

  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1
    
    it = self.head
    for _ in range(0, index):
      it = it.next
    
    return it.val

  def addAtHead(self, val: int) -> None:
    self.addAtIndex(0, val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
      return
    
    if index == 0:
      self.head = ListNode(val, None, self.head)
    else:
      it = self.head
      for _ in range(index - 1):
        it = it.next
      
      new = ListNode(val, it, it.next)
      it.next = new
      
      if new.next is not None:
        new.next.prev = new
      
    self.size += 1

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.size:
      return

    if index == 0:
      self.head = self.head.next
    else:
      it = self.head
      for _ in range(index - 1):
        it = it.next
      
      it.next = it.next.next
      if it.next is not None:
        it.next.prev = it
    
    self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)