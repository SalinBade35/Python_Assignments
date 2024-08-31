word = "NEPAL"

for i in range(len(word)):
    for j in range(len(word) - i):
        print(word[j], end="")
    print()
