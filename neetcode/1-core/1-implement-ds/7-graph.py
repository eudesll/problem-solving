class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = {}
    
        self.graph[src][dst] = 1

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph[src]:
            return False

        del self.graph[src][dst]
        if len(self.graph[src]) == 0:
            del self.graph[src]
            
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = {}
        level = []
        if src in self.graph:
            while dst not in self.graph[src]:
                visited[src] = 1
                for e in self.graph[src]:
                    if e not in visited:
                        level.append(e)
                
                src = -1
                while src not in self.graph:
                    if len(level) == 0:
                        return False

                    src = level.pop()

            return True
        return False

