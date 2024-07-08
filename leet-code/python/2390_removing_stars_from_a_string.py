class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c == "*":
                res.pop()
                continue
                
            res.append(c)
        
        return "".join(res)