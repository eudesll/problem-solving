class Solution:
  def calPoints(self, operations: List[str]) -> int:
    values = []
    for op in operations:
      if op == "+":
        values.append(values[-1] + values[-2])
      elif op == "D":
        values.append(values[-1] * 2)
      elif op == "C":
        values.pop(len(values) - 1)
      else:
        values.append(int(op))
    
    return sum(values)