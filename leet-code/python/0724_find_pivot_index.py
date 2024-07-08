class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls, rs = 0, sum(nums)
        for i, n in enumerate(nums):
            rs -= n
            if ls == rs:
                return i
            ls += n
        
        return -1