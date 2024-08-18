# grid 를 input으로 주면 폭탄을 설치하는 함수
def bomb_deploy(grid, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == -1:
                grid[i][j] = 0
            else:
                grid[i][j] += 1
    return grid

# grid 를 input으로 주면 폭탄이 터지는 함수
def bomb_explosion(grid, r, c):
    exploded = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:  # 폭탄이 터질 시간
                exploded[i][j] = True
                if can_go(i+1, j, r, c):
                    exploded[i+1][j] = True
                if can_go(i, j+1, r, c):
                    exploded[i][j+1] = True
                if can_go(i-1, j, r, c):
                    exploded[i-1][j] = True
                if can_go(i, j-1, r, c):
                    exploded[i][j-1] = True

    for i in range(r):
        for j in range(c):
            if exploded[i][j]:
                grid[i][j] = -1
            elif grid[i][j] != -1:
                grid[i][j] += 1
                
    return grid

# input grid를 변환하는 함수
def change_input(grid, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                grid[i][j] = -1
            else:
                grid[i][j] = 0
    return grid

# 해당좌표가 존재하는지 판단하는 함수
def can_go(x,y,r,c):
    return 0 <= x < r and 0 <= y < c

# 최종 grid를 변환하는 함수
def ret(grid, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == -1:
                grid[i][j] = '.'
            else:
                grid[i][j] = 'O'
    return grid

# 0초
r, c, n = map(int, input().split())
grid = [list(input()) for _ in range(r)]
grid = change_input(grid, r, c)

# 1초(가만히있기)
for i in range(r):
    for j in range(c):
        if grid[i][j] != -1:
            grid[i][j] += 1

# 2초부터 n초까지
for i in range(2, n+1):
    if i % 2 == 0:
        grid = bomb_deploy(grid, r, c)
    else:
        grid = bomb_explosion(grid, r, c)

# 최종 grid
grid = ret(grid, r, c)

# 출력
for row in grid:
    print(''.join(row))
