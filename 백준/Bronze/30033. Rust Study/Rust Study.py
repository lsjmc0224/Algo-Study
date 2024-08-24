N = int(input())
pages = list(map(int, input().split()))
studied = list(map(int, input().split()))

good = 0
for i in range(N):
    if studied[i] >= pages[i]:
        good += 1
print(good)