def part1(data):
  ans = 0
  for d in data:
    ans += 1 if d == '(' else -1
  
  return ans

def part2(data):
  location = 0
  for i, d in enumerate(data):
    location += 1 if d == '(' else -1
    if location == -1:
      return i + 1
  
  return -1

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_1_" + filename, "r")
    data = file.read()

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))