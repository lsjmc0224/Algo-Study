n = int(input())
arr = [[0]*100 for _ in range(100)]#도화지 전체 범위를 0으로 초기화

for _ in range(n): #n번 돌면서 row col 값을 받음
    y, x = map(int, input().split())
    
    #입력받은 범위 ~ +10 (총 변의 길이)를 돌면서 해당 자리에 1을 넣어줌
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
            
result = 0

for k in arr:
    result += k.count(1)
    
print(result)