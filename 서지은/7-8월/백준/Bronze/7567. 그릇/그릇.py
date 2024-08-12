lst = list(input().strip())

sm = 10
for i in range(1, len(lst)):
    if lst[i-1] == lst[i]:
        sm += 5
    else:
        sm += 10
print(sm)