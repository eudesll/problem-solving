class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums)
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                min_len = min(r - l + 1, min_len)
                cur_sum -= nums[l]
                l += 1

        if l == 0:
            return 0
            
        return min_len
