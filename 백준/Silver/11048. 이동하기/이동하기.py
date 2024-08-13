# i나 j 모두 현재 위치보다 작은 값으로는 이동할 수 없어서 사방탐색이라고 하기엔 애매함
# 이동할 수 있는 방향이 우, 하, 우하대각선 // 퍼져나가는 방식

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        dp[i][j] = maze[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[N-1][M-1])