# 1차원 dp table을 만들어서 lst안의 값과 비교하며 +1씩 해줌
# bfs에서 visited에 ci cj +1 해주는 그 느낌

N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

# 나보다 작은 값의 dp에 들어있는 숫자에 += 1
for n in range(1, N):
    ans = 0
    for k in range(n):
        if lst[n] > lst[k]:  # 현재의 숫자가 k번째의 숫자보다 클 때
            ans = max(ans, dp[k])
    dp[n] = ans + 1
    
ans = max(dp)
print(ans)