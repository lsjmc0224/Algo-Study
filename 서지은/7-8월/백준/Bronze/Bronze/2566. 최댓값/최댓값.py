nums = [list(map(int, input().split())) for _ in range(9)]

mx = 0
maxi, maxj = 0, 0
for i in range(9):
    for j in range(9):
        tmp = nums[i][j]
        mx = max(mx ,tmp)
        if mx == tmp:
            maxi = i+1
            maxj = j+1
            
print(mx)
print(maxi, maxj)