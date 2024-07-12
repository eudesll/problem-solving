class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]
            if total > k:
                r -= 1
            elif total < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        
        return res
        
