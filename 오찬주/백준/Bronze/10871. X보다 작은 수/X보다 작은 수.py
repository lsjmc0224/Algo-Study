n, x = map(int, input().split())

ans = list(map(int, input().split()))

#end = ' ' 를 하면 한줄로 출력 가능함
for i in range(n) :
  if (ans[i] < x) :
    print(ans[i], end=' ')