N = int(input())
lst = [float(input()) for _ in range(N)]

for i in range(1, N):
    # 현 위치와 전 위치*현 위치 값 중 더 큰 값을 lst[i]에 살려둠
    # for문 안에서 1.0 미만의 수와 만나더라도 그 전까지 곱했던 max 값이
    # lst 안에 살아있으므로 max(lst)로 곱의 최댓값을 꺼내주면 됨
    lst[i] = max(lst[i], lst[i]*lst[i-1])
ans = max(lst)

print(f"{ans:.3f}")