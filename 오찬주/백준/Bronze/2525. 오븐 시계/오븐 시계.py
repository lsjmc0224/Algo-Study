a, b = map(int, input().split())
c = int(input())

# 처음부터 a가 24보다 클 일이 없다 

if (b + c < 60) : print(a, b+c)
else :
  h = (b+c) / 60
  m = (b+c) % 60
  if(a+h >= 24): print(int(a+h)-24, m)
  else: print(int(a+h), m)