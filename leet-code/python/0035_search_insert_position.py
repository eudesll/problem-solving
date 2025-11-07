class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            idx = (r - l) // 2 + l
            if nums[idx] == target:
                return idx

            if nums[idx] > target:
                r = idx - 1
            else:
                l = idx + 1
        
        return l
            
        