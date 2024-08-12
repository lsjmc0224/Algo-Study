import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    #""안에 들어가있는 문자열과 합해줄 때는 +를 쓰고 그 외는 콤마로 연결 대신 , 사이는 공백 발생
    print("Case #"+str(i)+':',a+b)