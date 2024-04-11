class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    N = numCourses

    indegrees = [0] * N
    adj = defaultdict(list)
    for (from_node, to_node) in prerequisites:
      adj[from_node].append(to_node)
      indegrees[to_node] += 1
    
    q = deque()

    for node in range(N):
      if indegrees[node] == 0:
        q.append(node)
    
    res = []
    while q:
      node = q.popleft()
      res.append(node)

      for nei in adj[node]:
        indegrees[nei] -= 1
        if indegrees[nei] == 0:
          q.append(nei)
    
    return len(res) == N
      
    def checkRequirement(reqs, cycle=set()):
      for r in reqs:
        if r in cycle:
          return False
      
        if r in req_map:
          cycle.add(r)
          if not checkRequirement(req_map[r], cycle):
            return False
          cycle.remove(r)

      return True
    
    req_map = {}
    for pr in prerequisites:
      if pr[0] not in req_map:
        req_map[pr[0]] = set()
        
      req_map[pr[0]].add(pr[1])
      
    courses = list(req_map.keys())
    for c in courses:
      if not checkRequirement(req_map[c], set([c])):
        return False
      
      del req_map[c]
    
    return True