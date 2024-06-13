class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        arr1_count = defaultdict(int)
        end = []
        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            arr1_count[n] += 1
        
        end.sort()

        result = []
        for n in arr2:
            result += [n] * arr1_count[n]
        
        return result + end