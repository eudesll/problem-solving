class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        ones, zeros = 0, 0
        for i, n in enumerate(nums):
            if n == 0:
                while zeros == k:
                    zeros -= 1 if nums[i - ones] == 0 else 0
                    ones -= 1

                zeros += 1

            ones += 1
            res = max(res, ones)
        
        return res
            
            
