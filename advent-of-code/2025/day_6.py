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

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_6_" + filename, "r")
    data = file.read().split("\n")

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))