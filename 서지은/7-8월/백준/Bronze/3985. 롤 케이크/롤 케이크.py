L = int(input())
cake = [0]*(L+1)
N = int(input())
ans1 = ans2 = res1 = res2 = 0

for i in range(1, N+1):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        if cake[j] == 0:
            cake[j] = i
    temp = e-s+1
    if temp > res1:
        res1 = temp
        ans1 = i

for i in range(1, N+1):  # 실제로 가장 많이 받은 사람
    temp = cake.count(i)
    if temp > res2:
        res2 = temp
        ans2 = i

print(ans1, ans2, sep='\n')