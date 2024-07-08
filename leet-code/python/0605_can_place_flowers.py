class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f, s = flowerbed, len(flowerbed)
        for i in range(s):
            if f[i] == 0 and (i == 0 or i > 0 and f[i - 1] == 0) and (i == s - 1 or i < s - 1 and f[i + 1] == 0):
                n -= 1
                f[i] = 1
            
            if n <= 0:
                return True
        
        return False