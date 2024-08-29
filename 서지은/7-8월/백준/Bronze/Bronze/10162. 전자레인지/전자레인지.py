T = int(input())
temp = T

A = temp // 300
temp %= 300

B = temp // 60
temp %= 60

C = temp // 10
temp %= 10

if temp != 0:
    print(-1)
else: print(A, B, C)