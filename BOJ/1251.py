word = input()
possibles = []

l1, l2 = 0, 1

while l1 < len(word) - 2:
    l2 = l1 + 1

    while l2 < len(word) - 1:
        possibles.append("".join([word[:l1 + 1][::-1], word[l1 + 1:l2 + 1][::-1], word[l2 + 1:][::-1]]))

        l2 += 1
    
    l1 += 1

print(sorted(possibles)[0])