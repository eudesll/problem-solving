# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
      return None
    
    nodes = {}
    dq = deque()
    dq.append(node)
    while dq:
      n = dq.popleft()
      if n.val not in nodes:
        nodes[n.val] = Node(n.val)
        for neighbor in n.neighbors:
          dq.append(neighbor)
          nodes[n.val].neighbors.append(neighbor.val)
    
    for n in nodes:
      for i in range(len(nodes[n].neighbors)):
        n_val = nodes[n].neighbors[i]
        nodes[n].neighbors[i] = nodes[n_val]
    
    return nodes[node.val]