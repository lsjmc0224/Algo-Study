n = int(input())
pp = list(map(int, input().split()))

pp.sort()
answer = 0

for i in range(1, n+1):
    answer += sum(pp[0:i])
print(answer)