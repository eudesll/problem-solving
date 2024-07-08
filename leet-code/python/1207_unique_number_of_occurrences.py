class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurr = set()
        count = Counter(arr)

        for n in count:
            if count[n] in occurr:
                return False

            occurr.add(count[n])

        return True 