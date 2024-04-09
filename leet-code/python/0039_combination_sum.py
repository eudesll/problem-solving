class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def backtraking(start, target = target, cur = []):
      if target == 0:
        res.append(cur)
      if target <= 0:
        return

      for i in range(start, len(candidates)):
        backtraking(i, target - candidates[i], cur + [candidates[i]])
    
    backtraking(0)
      
    return res