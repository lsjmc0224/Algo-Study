n, m = map(int, input().split())
arr = [i for i in range(1, n+1)] #arr 길이 설정

for i in range(m):
    i, j = map(int, input().split())
    temp = arr[i-1:j]
    temp.reverse()
    arr[i-1:j] = temp
    
for i in range(n):
    print(arr[i], end = ' ')