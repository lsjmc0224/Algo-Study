word1 = input()
word2 = input()

lst = [0]*26
for n in word1:
    lst[ord(n)-97] += 1

for n in word2:
    lst[ord(n)-97] -= 1

res = 0
for n in lst:
    res += abs(n)
print(res)