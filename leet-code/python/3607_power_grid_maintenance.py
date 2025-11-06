class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        conns = list(range(c + 1))

        def find(x):
            while conns[x] != x:
                conns[x] = conns[conns[x]]
                x = conns[x]
            return x

        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                conns[rb] = ra

        next_node = [0] * (c + 1)
        comp_min = [0] * (c + 1)
        last = {}

        for i in range(1, c + 1):
            r = find(i)
            if comp_min[r] == 0:
                comp_min[r] = i
            else:
                next_node[last[r]] = i
            last[r] = i

        offline = [False] * (c + 1)
        res = []

        for o, x in queries:
            if o == 2:
                if offline[x]:
                    continue

                offline[x] = True
                r = find(x)
                if comp_min[r] == x:
                    y = next_node[x]
                    while y and offline[y]:
                        y = next_node[y]
                    comp_min[r] = y if y else 0

                continue
            
            if not offline[x]:
                res.append(x)
                continue
            
            r = find(x)
            res.append(comp_min[r] if comp_min[r] else -1)

        return res
        