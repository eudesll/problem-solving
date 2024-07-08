class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        keys = deque(rooms[0])
        while keys:
            k = keys.popleft()
            if k not in visited:
                visited.add(k)
                keys.extend(rooms[k])
        
        return len(visited) == len(rooms)
