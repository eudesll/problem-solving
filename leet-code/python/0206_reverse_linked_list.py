# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    current_node = head

    while current_node is not None:
      next_node = current_node.next
      current_node.next = prev_node
      prev_node = current_node
      current_node = next_node

    return prev_node
      
    # stack = []
    # while head is not None:
    #   stack.append(head)
    #   head = head.next
    
    # if len(stack) == 0:
    #   return None
    
    # head = stack.pop()
    # it = head
    # while len(stack) > 0:
    #   it.next = stack.pop()
    #   it = it.next
    # it.next = None
    
    # return head