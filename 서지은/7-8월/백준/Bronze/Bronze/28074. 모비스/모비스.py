word = list(input())
mobis = ['M', 'O', 'B', 'I', 'S']

for i in range(len(word)):
    if word[i] in mobis:
        mobis.remove(word[i])

if len(mobis) == 0:
    print("YES")
else: print("NO")