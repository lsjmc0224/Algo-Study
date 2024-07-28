# 1부터 n-1중에 2개를 고른다.
# 하나는 블루가 시작하는 행, 하나는 레드가 시작하는 행.

def return_two_rows(n):
    arr = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            arr.append([i,j])
    return arr

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for i in range(n)]
    arr = return_two_rows(n)
    cnt_arr = []
    for blue_start,red_start in arr:
        cnt = 0
        for i in range(0, blue_start):
            for j in range(m):
                if grid[i][j] != 'W':
                    cnt += 1
        
        for i in range(blue_start, red_start):
            for j in range(m):
                if grid[i][j] != 'B':
                    cnt += 1

        for i in range(red_start, n):
            for j in range(m):
                if grid[i][j] != 'R':
                    cnt += 1
        cnt_arr.append(cnt)
    print(f"#{_+1} {min(cnt_arr)}")