'''
함수로 잘 나눠서 풀어보기 !! ..
bfs로 4방 탐색
초기에 폭탄 입력 (1) -> (1초 후) 봄버맨 가마니
-> (1초 후) 빈 모든 칸에 폭탄 설치(2) -> (1초 후) 초기 폭탄(1) 사방 터짐
-> (1초 후) (1) 터진 자리에 전부 폭탄 설치 -> (1초 후) (2)때 설치된 폭탄 사방 터짐

2초, 4초에 설치 / 3초, 5초에 터짐 // 짝수 번째 초에 해당 초 -2초 전에 설치된 폭탄이 터짐
'''
from collections import deque
def bfs(si, sj, grid, visited):  # O 기준으로 사방에 있는 폭탄을 터트림
    q = deque()
    visited = [[0] * C for _ in range(R)]

    visited[si][sj] = 1
    grid[si][sj] = '.'
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                grid[ni][nj] = '.'  # 폭탄 터트려버리기


def make_bombs(grid):
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                grid[i][j] = 'O'

def bomb(grid):
    new_grid = [['O']* C for _ in range(R)]
    visited = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O' and not visited[i][j]:
                bfs(i, j, new_grid, visited)

    return new_grid


R, C, N = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 1

if N == 1:
    for lst in grid:
        print("".join(lst))

elif N % 2 == 0:
    for lst in [['O'] * C for _ in range(R)]:
        print("".join(lst))
else:
    first_bomb = bomb(grid)
    if (N//2) % 2 == 1:
        for lst in first_bomb:
            print("".join(lst))
    else:
        for lst in bomb(first_bomb):
            print("".join(lst))