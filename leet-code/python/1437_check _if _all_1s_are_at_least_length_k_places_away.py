class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous = -1
        for i, v in enumerate(nums):
            if v:
                if previous != -1 and i - (previous + 1) < k:
                    return False
                previous = i
            
        return True