# https://www.acmicpc.net/problem/10709

# h, w받기
h, w = map(int, input().split())

# grid 받기
grid = [list(input()) for i in range(h)]

# 결과그리드 세팅하기
res_grid = [[-1 for _ in range(w)] for _ in range(h)]

for row in range(h):
    for col in range(w):
        if grid[row][col] == 'c':
            res_grid[row][col] = 0
        else:
            if col == 0 or res_grid[row][col - 1] == -1:
                continue
            else:
                res_grid[row][col] = res_grid[row][col - 1] + 1

for i in range(h):
    print(' '.join(map(str, res_grid[i])))