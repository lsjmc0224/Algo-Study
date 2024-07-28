# SWEA 1210 ( https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh& )

# 사다리 그리드 가져와
# 자 이제 시작이야
# 첫번째 줄의 모든 수를 살펴보자
    # 만약 1이라면 자 이제 시작이야
        # initial을 따로 저장해라, ix, iy
        # 그 칸의 인덱스를 가져와라 x,y  = ix, iy
        # 동남서중 하나로만 이동해라 nx, ny = x + dxs(i), y + dys(i)
        #
        # 만약 nx가 101이라면 (x, y)가 1인지 2인지 확인해라.  
            # 그 칸이 2라면 iy를 출력해라 끝~~~

def dangchum_ladder(grid):
    dxs = [0, 0, 1]
    dys = [1, -1, 0]
    for i in range(0, 100):
        visited = [[0] * 100 for i in range(100)]
        ix, iy = 0, i
        x, y = 0, i
        if grid[x][y] == 1: # 사다리 시작조건
            while True: # 사다리 타기 시작
                visited[x][y] = 1
                if x == 99:
                    if grid[x][y] == 2: # 만약 x가 가장 마지막 줄이고 도착점이ㅏ라면
                        return(iy)
                    else:
                        break
                for j in range(3): # 동 서 남 순으로 학인
                    nx = x + dxs[j] # x, y 갱신
                    ny = y + dys[j]
                    if 0 <= nx < 100 and 0 <= ny < 100 and grid[nx][ny] and not visited[nx][ny]: # 해당 좌표로 갈 수 있다면 x,y 갱신
                        x,y = nx, ny
                        break  # 포문에서 나가기
    return None
for i in range(10):
    n = int(input())
    grid = [list(map(int, input().split())) for i in range(100)]
    print(f"#{n} {dangchum_ladder(grid)}")