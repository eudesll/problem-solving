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

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_7_" + filename, "r")
    data = file.read().split("\n")

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))