# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
      return None
    
    while len(lists) > 1:
      index = 0
      while index < len(lists):
        if index + 1 >= len(lists):
          break
        
        dummyNode = ListNode()
        it = dummyNode
        l1, l2 = lists[index], lists[index + 1]
        while l1 is not None and l2 is not None:
          if l1.val <= l2.val:
            it.next = ListNode(l1.val)
            l1 = l1.next
          else:
            it.next = ListNode(l2.val)
            l2 = l2.next
          it = it.next
        
        if l1 is not None:
          it.next = l1
        if l2 is not None:
          it.next = l2
        
        lists[index] = dummyNode.next
        del lists[index + 1]
        index += 1
    
    return lists[0]