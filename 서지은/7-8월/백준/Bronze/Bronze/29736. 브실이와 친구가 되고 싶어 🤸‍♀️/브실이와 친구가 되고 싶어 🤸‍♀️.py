A, B = map(int, input().split())
K, X = map(int, input().split())

ans = 0
# K와의 차이가 X보다 작거나 같은 사람만 친구의 자격이 있음
for i in range(A, B+1):
    if abs(K-i) <= X:
        ans += 1

if ans == 0:
    print("IMPOSSIBLE")
else:
    print(ans)