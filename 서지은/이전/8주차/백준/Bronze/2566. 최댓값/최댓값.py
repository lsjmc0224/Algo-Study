A = [list(map(int, input().split())) for _ in range(9)]
#9번 동안 돌면서 A 리스트 안에 값을 채워넣는 작업

maxi = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if maxi <= A[row][col]: #처음부터 돌리면서 max 값을 찾아줌
            maxi = A[row][col] #찾은 값이 max면 바로 maxi에 넣어줌
            max_row = row + 1 #순서대로 돌기 때문에 if문에 해당하면 돌던 row 값에 +1한 값을 넣어줌(1열부터 시작함)
            max_col = col + 1
print(maxi)
print(max_row, max_col)