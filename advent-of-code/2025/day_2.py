from collections import Counter 

def part1(data): # 1
  r = 0
  for d in data:
    ds = d.split("-")
    s, e = int(ds[0]), int(ds[1])
    for i in range(s, e + 1):
      n = str(i)

      if n[:len(n)//2] == n[len(n)//2:]:
        r += i
  
  return r

def part2(data): # 2
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

def __main__():
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_2_" + filename, "r")
    data = file.read().split(",")

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))

__main__()