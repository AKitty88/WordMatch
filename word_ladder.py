import re


def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, list):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in list]


def find(word, words, seen, target, path):
  list = []

  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)

  if len(list) == 0:
    return False

  list = sorted([(same(w, target), w) for w in list], reverse = True)

  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True

  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()


fname = input("Enter dictionary name: ")
file = open(fname)
lines = file.readlines()
currentPath: []
shortestPath: []

while True:
  start = input("Enter start word:")
  words = []

  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)

  target = input("Enter target word:")
  break

count = 0
currentPath = [start]
shortestPath = currentPath
seen = {start : True}

#while (count != 3):
if find(start, words, seen, target, currentPath):
  if (len(currentPath) == 0):
    print("No path found")
  elif (len(currentPath) >= len(shortestPath)):
    currentPath.append(target)
    print(len(currentPath) - 1, currentPath)
  else:
    shortestPath.append(target)
    print(len(shortestPath) - 1, shortestPath)

if (len(currentPath) == 0):
  print("No path found")