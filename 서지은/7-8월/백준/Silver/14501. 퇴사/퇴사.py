# T는 상담을 완료하기까지 걸리는 일자, P는 받을 수 있는 금액 // N일까지 일함
# 걸리는 일자와 금액을 2차원 배열  i, j에 위치하게 하고
# T + i부터 다시 탐색하도록 함 //
# 이후 종료부에서 max값 갱신

def dfs(n, sm):
    global ans
    
    if n > N:
        return

    if n == N:  # 퇴사일까지 n이 증가하면 종료
        ans = max(ans, sm)
        return

    if n+schedule[n][0] <= N:  # 일자만큼 더한 값이 N보다 작거나 같을 때
        dfs(n+schedule[n][0], sm+schedule[n][1])
    dfs(n+1, sm) # 외에는 n+1만 해줌


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# n은 일자, sm은 최대 수익
dfs(0, 0)
print(ans)