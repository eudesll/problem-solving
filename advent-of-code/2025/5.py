import os

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

example="""
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

expected=[3, 14]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "5_input"), "r")
  inputs = [example[1:].split("\n\n"), file.read().split("\n\n")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")