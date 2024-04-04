# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    while list1 is not None or list2 is not None:
      if list1 is not None and (list2 is None or list1.val < list2.val):
        stack.append(list1.val)
        list1 = list1.next
      else:
        stack.append(list2.val)
        list2 = list2.next
    
    if len(stack) == 0:
        return None

    head = ListNode(stack.pop(0))
    it = head
    while len(stack) > 0:
      it.next = ListNode(stack.pop(0))
      it = it.next
    
    return head