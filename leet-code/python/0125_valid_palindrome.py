class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return self.python_builtin(s)
        return self.two_pointers(s)

    def python_builtin(self, s:str) -> bool:
        clean_s = "".join(c for c in s.lower() if c.isalnum())
        return clean_s == clean_s[::-1]
    
    def two_pointers(self, s:str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
        
        return True