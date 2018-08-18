
def find(start, target, words):
    alpha = [chr(x) for x in range(97, 123)]
    seen = {start: None}
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


file = open("dictionary.txt")
lines = file.readlines()
words = []
start = input("Enter start word:")

for line in lines:
    word = line.rstrip()
    if len(word) == len("lead"):
        words.append(word)

target = input("Enter target word:")
print(find(start, target, words))