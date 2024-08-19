# n개의 정수로 이루어진 임의의 수열
# 연속된 몇 개의 수를 선택하여 구할 수 있는 합 중 가장 큰 합
# 수는 한 개 이상 선택

N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N
dp[0] = lst[0]

# i번째에 끝나는 연속 합의 최댓값
for i in range(1, N):
    if dp[i-1] + lst[i] > 0: # dp[i-1]의 값과 lst[i]의 합계 값이 양수라면 일단 더해볼만 함
        dp[i] = max(dp[i-1]+lst[i], lst[i])  # 그리고 현재 lst[i]값과 비교해서 더 큰 값을 dp[i]에 넣어줌
    else:
        dp[i] = lst[i]
ans = max(dp)
print(ans)