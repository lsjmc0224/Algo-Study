# 2xn 타일링 ( https://www.acmicpc.net/problem/11726 )
# input : n
n = int(input())
saero = [0, 1] + [0] * 999
garo = [0, 0] + [0] * 999

for i in range(2, n+1):
    saero[i] = saero[i-1] + garo[i-1]
    garo[i] = saero[i-1] 

# output : 2 * n크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지?
print((saero[n] + garo[n]) % 10007)