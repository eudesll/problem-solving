class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        pref_len = len(res)

        for s in strs[1:]:
            while res != s[:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                res = res[:pref_len]

        return res