class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                pos.append(i - len(pos))
        
        for p in pos:
            nums.pop(p)

        nums += [0] * len(pos)
        