N = int(input())
lst = list(map(int, input().split()))

total = 0

ys = 0
ms = 0
for i in range(N):
    temp = lst[i]
    ys += (temp//30+1) * 10
    ms += (temp//60+1) * 15

if ys > ms:
    print(f"M {ms}")
elif ys < ms:
    print(f"Y {ys}")
else: print(f"Y M {ms}")