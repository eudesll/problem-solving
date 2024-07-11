class Solution:
    def minOperations(self, logs: List[str]) -> int:
        main = 0
        for l in logs:
            if l == "./":
                continue
            
            if l == "../":
                main -= 1 if main > 0 else 0
            else:
                main += 1
        
        return main