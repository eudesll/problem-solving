class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def calc(pair):
            nonlocal s
            stack = []
            matches = 0
            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    matches += 1
                    stack.pop()
                else:
                    stack.append(c)
            
            s = "".join(stack)
            return matches

        res = 0
        pair = "ab" if x > y else "ba"
        res += calc(pair) * max(x,y)
        res += calc(pair[::-1]) * min(x,y)
        return res