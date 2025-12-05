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

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_4_" + filename, "r")
    data = file.read().split("\n")
    data = [list(d) for d in data]

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))