import re                                                                               # for regular expressions

# checks how many characters are the same in the item and target
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

# builds the list using the pattern; the list will contain all the words that are one letter different from the original word used in the pattern
def build(pattern, words, seen, list):
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in list]

# finds any path between start and target words; it might be the shortest path but there's no garantee for it
def find_any(word, words, seen, target, path):
  list = []

  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)                     # regular expression. The "." is present in the word in every position (one-by-one)

  if len(list) == 0:                                                                    #if the list is empty after building it -> there are no words one letter different from the word variable
    return False

  list = sorted([(same(w, target), w) for w in list], reverse = True)                   # arranges all the words in the list so that the ones with the most common letters come in the beginning of the list

  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:                                                      # if match should be the last item in the path before the target
        path.append(item)
      return True
    seen[item] = True

  for (match, item) in list:
    path.append(item)                                                                   # appends the item to the end of the path even though it might be wrong and might have to be removed (4 lines later)
    if find_any(item, words, seen, target, path):                                       # recursive; calls itself
      return True
    path.pop()                                                                          # removes the last element of the list because there is no next word (one letter from it) after this word

# finds shortest path between start and target words
def find_shortest(start, target, words, seen):
    alpha = [chr(x) for x in range(97, 123)]                                            # all the letters in the english alphabet
    queue = [start]                                                                     # the words in the path (including start and target)

    while queue:
        curr = queue.pop(0)                                                             # removes the element from the queue that was put in it last

        if curr == target:                                                              # if the actual (checked) word should be the last word in the path before the target
            path = []

            while curr:
                path.insert(0, curr)
                curr = seen[curr]

            return path

        letters = list(curr)                                                            # builds a list consisting of the letters of the current (checked) word

        for i, c in enumerate(letters):
            for letter in alpha:
                new_word = "".join(letters[:i]) + letter + "".join(letters[i+1:])       # tests all possible letter combinations that could be used

                if new_word in words and new_word not in seen:                          # checks if any of these possible letter combinations  (new_word) is in the dictionary; if yes it must not be in the seen dictionary
                    seen[new_word] = curr                                               # the word that passes these criteria gets saved in the seen dictionary
                    queue.append(new_word)                                              # the word that passes these criteria gets saved in the queue

file = open("dictionary.txt")
lines = file.readlines()
words = []
start = ""                                                                              # to make sure start will not be in the dictionary before the user gives a new start word
target = ""                                                                             # to make sure target will not be in the dictionary before the user gives a new target word

while start not in words:
    start = input("Enter start word:")

    for line in lines:
        word = line.rstrip()
        if len(word) == len(start):                                                     # if the word is as long as start
            words.append(word)                                                          # the variable words will only contain words that are the same lenght as the start variable

    if start not in words:                                                              # if start is not in the dictionary
        print(start, "is NOT a proper word!")
        path = []

while target not in words or len(target) != len(start):
    target = input("Enter target word (as long as the start word):")

    if len(target) == len(start) and target not in words:                               # if target is in the dictionary and the same length as start
        print(target, "is NOT a proper word!")
        path = []

assert len(start) == len(target)                                                        # target must be the same length as start

seen = {start: None}
seen[input("Words not allowed: ")] = None                                               # the not-allowed word (the user gives) gets saved in the seen dictionary

answer_yes = "y"
path_for_any = [start]                                                                  # path for the find_any function

if (input("Would you like the shortest possible path? y / any other key:   ")).lower() == answer_yes:               # if the user wants the shortest possible path, it'll be true
    path = find_shortest(start, target, words, seen)
    print(len(path) - 1, path)
else:                                                                                   # if the user does not want the shortest possible path, it'll be true
    if find_any(start, words, seen, target, path_for_any):
        path_for_any.append(target)                                                     # puts the target at the end of the path
        file.close()                                                                    # closes file
        print(len(path_for_any) - 1, path_for_any)
    else:
        file.close()                                                                    # closes file
        print("No path found")