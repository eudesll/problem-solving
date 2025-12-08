import os

def part1(data):
  ans = 0
  for y, d in enumerate(data):
    for x, c in enumerate(d):
      if c == "@":
        checks = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        count = 0
        for check in checks:
          if y + check[0] < 0 or y + check[0] >= len(data) or x + check[1] < 0 or x + check[1] >= len(d):
            continue
          
          count += 1 if data[y + check[0]][x + check[1]] == "@" else 0
        
        if count < 4:
          ans += 1

  return ans

def part2(data):
  previous, ans = -1, 0
  while previous != ans:
    removed, previous = set(), ans
    for y, d in enumerate(data):
      for x, c in enumerate(d):
        if c == "@":
          checks = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
          count = 0
          for check in checks:
            ny, nx = y + check[0], x + check[1]
            if ny < 0 or ny >= len(data) or nx < 0 or nx >= len(d):
              continue
            
            if data[ny][nx] == "@":
              count += 1
          
          if count < 4:
            removed.add((y, x))
            ans += 1
    
    for y, x in removed:
      data[y][x] = "."
      
  return ans

example="""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

expected=[13, 43]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "4_input"), "r")
  inputs = [example[1:].split("\n"), file.read().split("\n")]
  inputs = [[list(r) for r in input] for input in inputs]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")