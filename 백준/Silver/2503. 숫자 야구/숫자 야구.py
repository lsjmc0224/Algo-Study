# 111 ~ 999 까지 순열로 temp를 만든 뒤, 여기서 중복되는 수는 제외하고 주어진 s b 에 맞춰서 검사
# 검사에 통과한 녀석들만 ans.append 해주고, 한 자리씩 비교ㅛ하며 같을 때 cnt_s, cnt_b 올려주고
# 마지막에 각각의 cnt와 처음 입력받은 strike, ball과 비교해주기

import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

# 순열로 가능한 숫자를 모두 만든 뒤, s와 b에 따라서 맞는 수만 남김
for i in range(1, 10):  # 순열로 temp 수 만들어 줌
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k: continue

            for num in nums:
                n, strike, ball = num
                x, y, z = map(int, str(n))

                cnt_s, cnt_b = 0, 0

                if x == i:  # 하나를 기준으로 자릿 수와 숫자가 같으면 strike 올려주고
                    cnt_s += 1
                elif y == i or z == i:  # 다른 자릿수가 같으면 ball을 올려줌
                    cnt_b += 1

                if y == j:
                    cnt_s += 1
                elif x == j or z == j:
                    cnt_b += 1

                if z == k:
                    cnt_s += 1
                elif x == k or y == k:
                    cnt_b += 1

                if not (strike == cnt_s and ball == cnt_b):
                    break
            else:
                cnt += 1

print(cnt)