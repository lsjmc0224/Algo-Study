# LCD Test https://www.acmicpc.net/problem/2290

# s, n 받기
s, n = map(int, input().split())

# n 변환
n = list(map(int, str(n)))

# lcd 화면 grid 만들기
grid = [[' ' for _ in range((s + 2) * len(n) + len(n))] for _ in range((2*s + 3))]

for i in range(0, len(n)):
    num = n[i]
    start_col = i * ( s + 2 ) + i
    if num == 0:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = ' '
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)]  = '|'
    if num == 1:
        for row in range(1, 1 + s):
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col + (s + 1)]  = '|'
    if num == 2:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = '-'
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col] = '|'
    if num == 3:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = '-'
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col + (s + 1)]  = '|'
    if num == 4:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[s + 1][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col + (s + 1)]  = '|'
    if num == 5:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = '-'
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col + (s + 1)]  = '|'
    if num == 6:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = '-'
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)]  = '|'
    if num == 7:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col + (s + 1)]  = '|'
    if num == 8:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = '-'
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)]  = '|'
    if num == 9:
        for col in range(start_col + 1, start_col + (s + 2) - 1):
            grid[0][col] = '-'
            grid[s + 1][col] = '-'
            grid[2 * (s + 1)][col] = '-'
        for row in range(1, 1 + s):
            grid[row][start_col] = '|'
            grid[row][start_col + (s + 1)] = '|'
        for row in range(s + 2, s + 2 + s):
            grid[row][start_col + (s + 1)]  = '|'
for row in grid:
    print(''.join(row))