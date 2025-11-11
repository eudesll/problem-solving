class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #return self.my_solution(nums, k)
        return self.cleaner(nums, k)

    def my_solution(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        l = 0
        for n in nums:
            if count[n]:
                return True
            
            count[n] += 1
            if len(count) > k:
                del count[nums[l]]
                l += 1
        
        return False

    def cleaner(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            
            seen[val] = i
        
        return False
            