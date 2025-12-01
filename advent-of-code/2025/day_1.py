def stop_on_zero(data): # 1
  dial, r = 50, 0
  for d in data:
    dial += (int(d[1:]) if d[0] == "R" else -int(d[1:]))

    r += 0 if dial % 100 else 1
  
  return r

def pass_through_zero(data): # 2
  dial, r = 50, 0
  for d in data:
    val = int(d[1:]) if d[0] == "R" else -int(d[1:])
    dial += val

    if val > 0:
        r += dial // 100 - (dial - val) // 100
    elif val < 0:
        r += (dial - val - 1) // 100 - (dial - 1) // 100
  
  return r

def __main__():
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("day_1_" + filename, "r")
    data = file.read().split("\n")

    print(filename)
    print(f"- 1:", stop_on_zero(data))
    print(f"- 2:", pass_through_zero(data))

__main__()