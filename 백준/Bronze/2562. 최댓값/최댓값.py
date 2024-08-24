nums = []
ans = 0
temp = 0
for i in range(9):
    n = int(input())
    temp = max(n, temp)
    if n == temp:
        ans = i+1

print(temp, ans, sep="\n")