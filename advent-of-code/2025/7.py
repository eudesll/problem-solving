import os
from collections import defaultdict

def part1(data):
  ans = 0
  ray = {i for i, v in enumerate(data[0]) if v == 'S'}
  for i in range(1, len(data)):
    split = []
    for r in ray:
      if data[i][r] == "^":
        split.append(r)
    
    for r in split:
      ans += 1
      ray.add(r - 1)
      ray.add(r + 1)
      ray.remove(r)

  return ans

def part2(data):
  ray = defaultdict(int)
  for i, v in enumerate(data[0]):
    if v == 'S':
      ray[i] = 1
  
  for i in range(1, len(data)):
    split = []
    for r in ray:
      if data[i][r] == "^":
        split.append(r)
    
    for r in split:
      ray[r - 1] += ray[r]
      ray[r + 1] += ray[r]
      ray.pop(r)

  return sum([ray[x] for x in ray])

example="""
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

expected=[21, 40]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "7_input"), "r")
  inputs = [example[1:].split("\n"), file.read().split("\n")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")