N = int(input())
K = list(input())

odd, even = 0, 0
for i in range(N):
    if int(K[i])%2 == 0:
        even += 1
    else: odd += 1

if even > odd:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)