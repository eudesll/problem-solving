import os

def part1(data):
  dial, r = 50, 0
  for d in data:
    dial += (int(d[1:]) if d[0] == "R" else -int(d[1:]))

    r += 0 if dial % 100 else 1
  
  return r

def part2(data):
  dial, r = 50, 0
  for d in data:
    val = int(d[1:]) if d[0] == "R" else -int(d[1:])
    dial += val

    if val > 0:
        r += dial // 100 - (dial - val) // 100
    elif val < 0:
        r += (dial - val - 1) // 100 - (dial - 1) // 100
  
  return r

example="""
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

expected=[3, 6]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "1_input"), "r")
  inputs = [example[1:].split("\n"), file.read().split("\n")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")