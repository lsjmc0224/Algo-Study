# 계단 시작점부터 계단 꼭대기까지
# 해당 계단을 밟으면 계단에 쓰여있는 점수를 받게 됨
# 연속된 3개의 계단을 밟을 수는 없음
# 마지막 계단은 반드시 밟아야 함 // N에서 끝내야 함
# dp를 2차원 배열로 만들어서 안 밟았을 때, 1번, 2번의 값을 각각 넣어준 뒤
# 마지막 행에서 max값 갱신

N = int(input())
stairs = [int(input()) for _ in range(N)]  # 1차원 배열로 계단을 받음
dp = [[0]*3 for _ in range(N)]
dp[0][1] = stairs[0]  # 계단 마지막은 반드시 들어가야 하므로 역으로 더해주며 시작

# 계단 시작이 아닌 끝에서부터 출발하여 누적합
for i in range(1, N):
    dp[i][0] = max(dp[i-1][1:3])
    dp[i][1] = dp[i-1][0] + stairs[i]
    dp[i][2] = dp[i-1][1] + stairs[i]

ans = max(dp[N-1][1:3])
print(ans)