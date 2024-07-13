class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        index_map = {r:i for i, r in enumerate(positions)}

        stack = []
        for p in sorted(positions):
            i = index_map[p]
            if directions[i] == "R":
                stack.append(i)
                continue

            while stack and healths[i]:
                i2 = stack.pop()
                if healths[i] == healths[i2]:
                    healths[i] = healths[i2] = 0
                elif healths[i] > healths[i2]:
                    healths[i] -= 1
                    healths[i2] = 0
                else:
                    healths[i] = 0
                    healths[i2] -= 1
                    stack.append(i2)

        return [h for h in healths if h > 0]