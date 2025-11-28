class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                break
            
            l += 1 if sum < target else 0
            r -= 1 if sum > target else 0
        
        return [l + 1, r + 1]