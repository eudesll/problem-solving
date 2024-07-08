class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ct in t:
            if i == len(s):
                break 

            if ct == s[i]:
                i += 1
            
        return i == len(s)