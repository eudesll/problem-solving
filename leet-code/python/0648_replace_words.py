class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wordsDict = set()
        for entry in dictionary:
            wordsDict.add(entry)

        words = sentence.split()
        for idx, w in enumerate(words):
            for i in range(len(w)):
                if w[:i] in wordsDict:
                    words[idx] = w[:i]
                    break
        
        return " ".join(words)