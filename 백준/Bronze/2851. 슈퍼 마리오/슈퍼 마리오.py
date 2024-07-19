tot = 0
arr = []
for _ in range(10):
    arr.append(int(input()))

for i in arr:
    tot += i
    if tot >= 100:
        if tot - 100 > 100 -(tot-i):
            tot -= i
            break
print(tot)