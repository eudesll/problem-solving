class Solution:
  def isValid(self, s: str) -> bool:
    bracketMatch = { "}": "{", "]": "[", ")": "(" }
    stack = []
    
    for c in s:
      if c in bracketMatch and len(stack) > 0:
        if bracketMatch[c] != stack[-1]:
          return False
        
        stack.pop()
      else:
        stack.append(c)
      
    return len(stack) == 0