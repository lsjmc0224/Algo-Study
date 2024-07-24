n = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(n):
    h, w = map(int, input().split())

    for i in range(h, h+10):
        for j in range(w, w+10):
            arr[i][j] = 1
    res = 0
    for k in arr:
        res += k.count(1)

print(res)