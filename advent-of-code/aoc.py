import os
import sys
from pathlib import Path

template = """
def part1(data):
  return 0

def part2(data):
  return 0
  
if __name__ == "__main__":
  filenames = ["test", "input"]
  for filename in filenames:
    file = open("{day}_" + filename, "r")
    data = file.read().split("\\n")

    print(filename)
    print(f"- 1:", part1(data))
    print(f"- 2:", part2(data))"""

def get(year, day):
  dir = os.path.dirname(__file__)
  dir = os.path.join(dir, year)
  if not os.path.isdir(dir):
    os.mkdir(dir)
  
  filepath = os.path.join(dir, day + ".py")
  if not os.path.isfile(filepath):
    f = open(filepath, "w")
    f.write(template[1:].replace("{day}", day))
    f.close()

  inputs = ["test", "input"]
  for input in inputs:
    input_path = os.path.join(dir, day + "_" + input)
    if not os.path.isfile(input_path):
      f = open(input_path, "w")
      f.close()

if __name__ == '__main__':
  get(sys.argv[1], sys.argv[2])

# TODO:
# 1- get input data from aoc
# 2- find a better way to execute the challenge code