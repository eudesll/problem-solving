import os
import math

def part1(data):
  data = [d.split() for d in data]
  ans = [1 if s == '*' else 0 for s in data[-1]]
  for d in data:
    if d[0] in ['*', '+']:
      continue

    for i in range(len(d)):
      if data[-1][i] == '*':
        ans[i] *= int(d[i])
        continue
      
      ans[i] += int(d[i])

  return sum(ans)

def part2(data):
  signs = data[-1].split()
  agg = [[] for _ in range(len(signs))]
  ans_i = len(agg) - 1

  for i in range(len(data[0]) - 1, -1, -1):
    col = ""
    for j in range(len(data) - 1):
      col += data[j][i]
    
    if col.strip() == "":
      ans_i -= 1
      continue

    agg[ans_i].append(int(col.strip()))
  
  ans = 0
  for i, nums in enumerate(agg):
    if signs[i] == '*':
      v = math.prod(nums)
    else:
      v = sum(nums)
    
    ans += v

  return ans

example="""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

expected=[4277556, 3263827]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "6_input"), "r")
  inputs = [example[1:].split("\n"), file.read().split("\n")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")