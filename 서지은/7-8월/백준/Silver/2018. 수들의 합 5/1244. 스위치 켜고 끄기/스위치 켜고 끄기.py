def change_boy(n):
    for i in range(1, N+1):  # 1번~N번 스위치까지
        if i % n == 0: # 스위치 번호가 받은 숫자의 배수일 때
            if lst[i-1] == 0: lst[i-1] = 1
            else: lst[i-1] = 0  # 스위치 상태 바꿈

def change_girl(n):   # 가장 넓은 구간이면 모든 숫자가 대칭하지 않더라도 ..
    center = n-1
    if lst[center] == 0:
        lst[center] = 1
    else:
        lst[center] = 0
    # 받은 숫자의 idx
    for i in range(1, N//2):
        if 0 <= (center-i) and (center+i) < N:
            if lst[center-i] != lst[center+i]: return
            elif lst[center-i] == lst[center+i] == 0:
                lst[center-i] = lst[center+i] = 1
            elif lst[center-i] == lst[center+i] == 1:
                lst[center-i] = lst[center+i] = 0


N = int(input())
lst = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:  # 남학생일 경우
        change_boy(num)
    elif gender == 2:  # 여학생일 경우
        change_girl(num)

for i in range(0, N, 20):
    print(*lst[i:i+20])