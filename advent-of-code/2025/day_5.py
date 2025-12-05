import sys
from collections import defaultdict

def part1(data):
  fresh = build_fresh_map(data[0])
  ans = 0
  ingredients = map(int, data[1].splitlines())
  for i in ingredients:
    for s, e in fresh.items():
      if i >= s and i <= e:
        ans += 1
        break

  return ans

def part2(data):
  fresh = build_fresh_map(data[0])
  ans = 0
  for s, e in fresh.items():
    ans += (e - s + 1)

  return ans

def build_fresh_map(data):
  fresh = [(int(lower), int(upper)) for lower, upper in (f.split("-") for f in data.splitlines())]
  fresh.sort(key=lambda x: x[0])

  i, to_remove = 0, []
  while i < len(fresh) - 1:
    s, e = fresh[i]
    for j in range(i + 1, len(fresh)):
      ns, ne = fresh[j]
      if ns > e:
        break
      to_remove.append(j)
      e = max(e, ne)
    
    fresh[i] = (s, e)
    i = j
  
  for i in to_remove[::-1]:
    fresh.pop(i)

  return dict(fresh)

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_5_" + filename, "r")
    data = file.read().split("\n\n")

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))