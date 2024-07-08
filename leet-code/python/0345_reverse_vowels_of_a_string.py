class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"])
        sv = []
        for c in s:
            if c in vowels:
                sv.append(c)
        
        res = []
        for i in range(len(s)):
            c = s[i]
            if c in vowels:
                c = sv.pop()
            res.append(c)

        return "".join(res)