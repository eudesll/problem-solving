import os

def part1(data):
  ans = 0
  for d in data:
    higher = 0
    l, r = 0, 1
    while l < len(d):
      if l != r:
        higher = max(higher, int(d[l] + d[r]))

      if r < len(d) - 1 and (d[l] >= d[r] or l == r):
        r += 1
      else:
        l += 1

    ans += higher
  
  return ans

def part2(data):
  ans = 0
  for d in data:
    stack = []
    for i, v in enumerate(d):
      while stack and int(stack[-1]) < int(v) and len(stack) + len(d) - i > 12:
        stack.pop()

      stack.append(v)

    ans += int("".join(stack[:12]))

  return ans

example="""
987654321111111
811111111111119
234234234234278
818181911112111"""

expected=[357, 3121910778619]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "3_input"), "r")
  inputs = [example[1:].split("\n"), file.read().split("\n")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")