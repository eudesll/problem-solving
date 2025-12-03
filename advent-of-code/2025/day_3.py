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

if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_3_" + filename, "r")
    data = file.read().split("\n")

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))