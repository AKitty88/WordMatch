import re

def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in list]

def find_any(word, words, seen, target, path):
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
    if find_any(item, words, seen, target, path):
      return True
    path.pop()

def find_shortest(start, target, words, seen):
    alpha = [chr(x) for x in range(97, 123)]
    queue = [start]

    while queue:
        curr = queue.pop(0)

        if curr == target:
            path = []

            while curr:
                path.insert(0, curr)
                curr = seen[curr]

            return path

        letters = list(curr)

        for i, c in enumerate(letters):
            for letter in alpha:
                new_word = "".join(letters[:i]) + letter + "".join(letters[i+1:])

                if new_word in words and new_word not in seen:
                    seen[new_word] = curr
                    queue.append(new_word)

def main_for_test(start, target, not_allowed, shortest):
    file = open("dictionary.txt")
    lines = file.readlines()
    words = []

    for line in lines:
        word = line.rstrip()
        if len(word) == len(start):
            words.append(word)

    seen = {start: None}
    seen[not_allowed] = None

    answer_yes = "y"
    path_for_any = [start]

    if shortest.lower() == answer_yes:
        path = find_shortest(start, target, words, seen)
        return path
    else:
        if find_any(start, words, seen, target, path_for_any):
            path_for_any.append(target)
            return path_for_any
        else:
            path = "No path found"
            return path
