class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #return self.kadane(nums)
        return self.divide_conquer(nums)

    def kadane(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum + n, n)
            maxSum = max(maxSum, curSum)
        
        return maxSum

    # Preffix and Suffix max sub arrays
    def divide_conquer(self, nums: List[int]) -> int:
        N = len(nums)
        pre, suf = [*nums], [*nums]
        for i in range(1, N):
            pre[i] += max(0, pre[i - 1])
            suf[N - 1 - i] += max(0, suf[N - i])

        def find_subarray(nums, l, r):
            if l == r:
                return nums[l]
            
            mid_idx = (l + r) // 2
            left = find_subarray(nums, l, mid_idx)
            right = find_subarray(nums, mid_idx + 1, r)
            mid = pre[mid_idx] + suf[mid_idx + 1]

            return max(left, right, mid)
        
        return find_subarray(nums, 0, N - 1)