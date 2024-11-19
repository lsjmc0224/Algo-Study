# N  (사람 수)
# 잔고
# J (당첨 금)
# C (주 수)

N = int(input())
curr_jango = list(map(int, input().split()))
J = int(input())
C = int(input())

# 강호 잔고 1차원 배열
def mean_jango(N, curr_jango, J, C):
    dp = [curr_jango] + [[0 for _ in range(N)] for _ in range(C)]

    for i in range(1, C + 1):
        for j in range(N):
            dp[i][j] = dp[i-1][j] + J / sum(dp[i-1]) * dp[i-1][j]
    
    # 강호 잔고
    return dp[C][0]

ret = mean_jango(N, curr_jango, J, C) 
print(ret)