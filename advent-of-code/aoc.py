import os
import sys
import requests
from datetime import datetime

base_url = ""

template = """
import os

def part1(data):
  return -1

def part2(data):
  return -1

example=\"""
\"""

expected=[0, 0]

if __name__ == "__main__":
  dir = os.path.dirname(__file__)
  file = open(os.path.join(dir, "{day}_input"), "r")
  inputs = [example[1:].split("\\n"), file.read().split("\\n")]
  
  for i, p in enumerate([part1, part2]):
    res = p(inputs[0])
    if res != expected[i]:
      print(f"{i + 1}: {res}, should be {expected[i]}")
      break
    
    print(f"{i + 1}: {p(inputs[1])}")"""

def setup(year, day):
  challenge, input = build_paths(year, day)
  
  dir = os.path.dirname(challenge)
  if not os.path.isdir(dir):
    os.mkdir(dir)
  
  if not os.path.isfile(challenge):
    f = open(challenge, "w")
    f.write(template[1:].replace("{day}", day))
    f.close()

  if not os.path.isfile(input):
    f = open(input, "w")
    f.write(get_input_data())
    f.close()

def get_input_data():
  dir = os.getcwd()
  session_file = os.path.join(dir, ".session")
  if not os.path.isfile(session_file):
    print("empty input, no session file set")
    return ""
  
  f = open(session_file, "r")
  headers = {"Cookie": f.read()}
  f.close()

  url = base_url + "/input"
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.text[:-1]
  else:
    print(f"we had a problem getting the input data ({response.status_code})")
  
  return ""


def validate_date(year, day):
  year, day = int(year), int(day)
  if year < 2015:
    print("invalid year, advent of code started on 2015")
    return False
  
  today = datetime.today()
  if year > today.year:
    print("invalid year, did you come from the future?")
    return False
  
  if day < 1:
    print("invalid day, are you trying to break something?")
    return False
  
  if year == today.year and day > today.day:
    print("invalid day, can you try this same command tomorrow?")
    return False

  if day > 25:
    print("invalid day, Santa worked a lot last night, give him a break")
    return False

  return True

def build_paths(year, day):
  dir = os.path.dirname(__file__)
  dir = os.path.join(dir, year)

  return [os.path.join(dir, day + p) for p in [".py", "_input"]]

if __name__ == '__main__':
  year, day = sys.argv[1:]
  if not validate_date(year, day):
    os._exit(1)
  
  base_url = f"https://adventofcode.com/{year}/day/{day}"
  setup(year, day)
  print(base_url)
