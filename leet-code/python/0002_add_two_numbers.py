# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = False
    rr = ListNode()
    cr = rr
    while l1 is not None:
      if carry:
        cr.val += 1
        carry = False
        
      cr.val += l1.val
      if l2 is not None:
        cr.val += l2.val
      
      if cr.val >= 10:
        carry = True
        cr.val = cr.val % 10
      
      l1 = l1.next
      if l2 is not None:
        l2 = l2.next
      
      if l1 is None and l2 is not None:
        l1 = l2
        l2 = None
      
      if l1 is None:
        break
      
      cr.next = ListNode()
      cr = cr.next
      
    if carry:
      cr.next = ListNode(1)
      
    return rr
        