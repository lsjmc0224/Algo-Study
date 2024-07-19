n, m = map(int, input().split())
arr_1 = []
arr_2 = []

for _ in range(n):
    a = list(map(int, input().split()))
    arr_1.append(a)

for _ in range(n):
    b = list(map(int, input().split()))
    arr_2.append(b)

for i in range(n):
    for j in range(m):
        print(arr_1[i][j] + arr_2[i][j], end=" ")
    print()