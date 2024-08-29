N = int(input())
menu = [0]*(N+1)
total = 0

for i in range(1, N+1):
    menu[i] = int(input())

M = int(input())
for i in range(M):
    num = int(input())
    total += menu[num]

print(total)