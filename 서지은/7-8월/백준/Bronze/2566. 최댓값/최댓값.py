arr = [list(map(int, input().split())) for _ in range(9)]
res = 0
a, b = 0, 0

for i in range(9):
    for j in range(9):
        if res <= arr[i][j]:
            res = arr[i][j]
            a = i+1
            b = j+1

print(res)
print(a, b)