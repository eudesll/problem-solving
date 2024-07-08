class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        res = [n + extraCandies >= highest for n in candies]
        return res