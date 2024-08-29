X = int(input())
N = int(input())

total = 0

for i in range(1, N+1):
  a, b = map(int,input().split())
  total += a*b

if (total == X) : print('Yes')
else: print('No')