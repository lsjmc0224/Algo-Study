H, W = map(int, input().split())

lst = [[-1]*W for _ in range(H)]
arr = [input().strip() for _ in range(H)]

for i in range(H):
    cnt = -1
    for j in range(W):
        if arr[i][j] == 'c':
            lst[i][j] = 0
            cnt = 0

        elif cnt >= 0:
            cnt += 1
            lst[i][j] = cnt

for n in lst:
    print(" ".join(map(str, n)))