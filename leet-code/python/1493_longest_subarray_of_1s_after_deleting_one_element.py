# Equals to 1004
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        ones, zeros, k = 0, 0, 1
        for i, n in enumerate(nums):
            if n == 0:
                while zeros == k:
                    zeros -= 1 if nums[i - ones] == 0 else 0
                    ones -= 1

                zeros += 1

            ones += 1
            res = max(res, ones)
        
        return res - 1