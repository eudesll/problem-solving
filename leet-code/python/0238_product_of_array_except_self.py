class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre, suf = 1, 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
            res[len(nums) - i - 1] *= suf
            suf *= nums[len(nums) - i - 1]
        
        return res