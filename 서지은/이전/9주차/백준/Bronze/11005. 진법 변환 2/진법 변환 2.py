arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())
result = ''

while n!=0:
    result += str(arr[n%b])
    n = n // b

print(result[::-1])