n = int(input())
m = int(input())
arr = []

for i in range(n, m+1):
    if i>1:
        sosu = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                sosu = False
                break
        if sosu:
            arr.append(i)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)