# 사각형의 크기는 2*n
N = int(input())
dp = [0] * (N+1)

dp[0] = 1
dp[1] = 3

for n in range(2, N+1):
    dp[n] = dp[n-2]*2 + dp[n-1]

print(dp[N-1]%10007)