class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        highestAvg = windowSum / k
        for i in range(1, len(nums) - k + 1):
            windowSum -= nums[i - 1] 
            windowSum += nums[i + k - 1]
            if windowSum / k > highestAvg:
                highestAvg = windowSum / k
        
        return highestAvg
