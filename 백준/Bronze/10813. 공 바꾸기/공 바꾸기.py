n, m = map(int, input().split())
arr = []

for i in range(1, n+1):
    arr.append(i)

for j in range(m):
    x, y = map(int, input().split())
    arr[x-1], arr[y-1] = arr[y-1], arr[x-1]

result = " ".join([str(_) for _ in arr])
print(result)