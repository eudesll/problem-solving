def part1(data):
  x = y = 0
  dir = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}
  visited = set([(x,y)])
  for d in data:
    x += dir[d][0]
    y += dir[d][1]
    visited.add((x, y))

  return len(visited)

def part2(data):
  x = y = rx = ry = 0
  dir = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}
  visited = set([(x,y)])
  for i, d in enumerate(data):
    if i % 2 == 0:
      x += dir[d][0]
      y += dir[d][1]
      visited.add((x, y))
    else:
      rx += dir[d][0]
      ry += dir[d][1]
      visited.add((rx, ry))
    

  return len(visited)

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_3_" + filename, "r")
    data = file.read()

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))