class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = highest = 0
        for d in gain:
            curr += d

            highest = max(highest, curr)
        
        return highest