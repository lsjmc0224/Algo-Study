# 골드바흐 파티션 ( https://www.acmicpc.net/problem/17103 )
# input : 테스트 케이스 개수 T와 T개의 숫자들
import sys
input = sys.stdin.readline

# 짝수 미리 erra에 넣어놓기
erra = [0,0,1] + [1,0] * 499999

# 홀수만 for문 돌리기
for i in range(3, int(1000000**(1/2)) + 1, 2):
    if erra[i] == 0:
        continue
    else:
        for j in range(i*i, 1000000, i):
            erra[j] = 0
# 소수 리스트 작성
prime = [i for i,x in enumerate(erra) if x]

# 해보자
T = int(input())
for _ in range(T):
    inp = int(input())
    count = 0
    for k in prime:
        if k > inp//2:
            break
        else: 
            if erra[inp - k]:
                count += 1

    print(count)