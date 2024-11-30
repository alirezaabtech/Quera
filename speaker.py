# بلندگو
# https://quera.org/problemset/3430

word_spoken = input()
word_spoken = list(word_spoken)

for i in range(len(word_spoken)):
    for j in range(i,-1,-1):
        word_spoken[j] = word_spoken[i]
    print(''.join(word_spoken))