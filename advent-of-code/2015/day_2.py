def part1(data):
  ans = 0
  for d in data:
    l, w, h = map(int, d)
    ans += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    
  return ans

def part2(data):
  ans = 0
  for d in data:
    l, w, h = map(int, d)
    smallest = min(2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l)
    ans += smallest + l * w * h

  return ans

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_2_" + filename, "r")
    data = file.read().split("\n")
    data = [(d.split("x")) for d in data]

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))