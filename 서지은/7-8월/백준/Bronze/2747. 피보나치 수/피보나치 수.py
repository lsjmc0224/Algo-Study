N = int(input())
dp = [0]*(N+1)  # dp 테이블 초기화
dp[0] = 0
dp[1] = 1

for n in range(2, N+1):
    dp[n] = dp[n-1] + dp[n-2]
    # n-1 과 n-2를 더한 값이 현재의 n

print(dp[N])