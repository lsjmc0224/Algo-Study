import sys
input = sys.stdin.readline

nums = []

for i in range(9):
    nums.append(int(input()))
    #append는 무조건 str 형식으로 저장 int로 저장하려면 변환해서 저장해줘야 함
       
print(max(nums))
print(nums.index(max(nums))+1)