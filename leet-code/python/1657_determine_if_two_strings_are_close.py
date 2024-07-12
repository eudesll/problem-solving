class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1, c2 = Counter(word1), Counter(word2)
        qMap1, qMap2 = defaultdict(int), defaultdict(int)
        for c in c1:
            if c not in c2:
                return False
            
            qMap1[c1[c]] += 1
            qMap2[c2[c]] += 1
        
        for q in qMap1:
            if q not in qMap2 or qMap1[q] != qMap2[q]:
                return False

        return True