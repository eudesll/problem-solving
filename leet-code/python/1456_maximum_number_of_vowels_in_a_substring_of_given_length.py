class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        res, curr = 0, 0
        for i, c in enumerate(s):
            if i >= k:
                curr -= 1 if s[i-k] in vowels else 0
            
            curr += 1 if c in vowels else 0
            res = max(res, curr)
        
        return res