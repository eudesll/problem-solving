class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        
        if len(word1) > len(word2):
            res.append(word1[len(word2):])
        if len(word2) > len(word1):
            res.append(word2[len(word1):])
        
        return "".join(res)