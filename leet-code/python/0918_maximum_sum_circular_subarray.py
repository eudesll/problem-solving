class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #return self.pre_suf(nums)
        return self.minimum_subarray(nums)

    def pre_suf(self, nums: List[int]) -> int:
        suf = [*nums]
        sufSum = suf[-1]
        for i in range(len(nums) - 2, -1, -1):
            sufSum += suf[i]
            suf[i] = max(sufSum, suf[i + 1])
        
        maxSum = nums[0]
        wrapSum = nums[0]
        curSum = 0
        pre = 0
        for i in range(len(nums)):
            curSum = max(curSum, 0) + nums[i]
            maxSum = max(maxSum, curSum)

            pre += nums[i]
            if i + 1 < len(nums):
                wrapSum = max(wrapSum, pre + suf[i + 1])

        return max(maxSum, wrapSum)

    def minimum_subarray(self, nums: List[int]) -> int:
        maxCurSum = 0
        maxSum = nums[0]
        minCurSum = 0
        minSum = nums[0]
        totalSum = 0
        for n in nums:
            maxCurSum = max(maxCurSum, 0) + n
            maxSum = max(maxSum, maxCurSum)
            
            minCurSum = min(minCurSum, 0) + n
            minSum = min(minSum, minCurSum)

            totalSum += n
        
        if totalSum == minSum:
            return maxSum

        return max(maxSum, totalSum - minSum)