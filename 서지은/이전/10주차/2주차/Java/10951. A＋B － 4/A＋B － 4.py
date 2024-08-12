import sys
input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
#무한루프 돌 때(끝나는 시점이 정해져 있지 않을 때)에는 try와
#입력이 끝난 걸 가리키는 except 로 break 넣어주기