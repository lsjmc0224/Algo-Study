total = int(input())
N = int(input())

sm =  0
for _ in range(N):
    price, num = map(int, input().split())
    sm += price * num

if sm == total:
    print("Yes")
else:
    print("No")