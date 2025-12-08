import os

def part1(data):
  r = 0
  for d in data:
    ds = d.split("-")
    s, e = int(ds[0]), int(ds[1])
    for i in range(s, e + 1):
      n = str(i)

      if n[:len(n)//2] == n[len(n)//2:]:
        r += i
  
  return r

def part2(data):
  r = 0
  for d in data:
    ds = d.split("-")
    s, e = int(ds[0]), int(ds[1])
    for num in range(s, e + 1):
      n = str(num)

      for i in range(len(n) // 2, 0, -1):
        sub = n[0:i]
        if len(n) % i != 0:
          continue

        for j in range(i, len(n), i):
          if n[j:j+i] != sub:
            sub = False
            break

        if sub:
          r += num
          break
  
  return r

example="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

expected=[1227775554, 4174379265]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "2_input"), "r")
  inputs = [example.split(","), file.read().split(",")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")