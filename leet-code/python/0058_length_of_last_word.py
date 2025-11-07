class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)
        while s[r - 1] == " ":
            r -= 1
        
        l = r
        while l > 0 and s[l - 1] != " ":
            l -= 1
        
        return len(s[l:r])
        