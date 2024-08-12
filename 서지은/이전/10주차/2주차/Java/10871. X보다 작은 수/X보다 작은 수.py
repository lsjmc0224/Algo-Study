import sys
input = sys.stdin.readline

n, x = map(int, input().split())
num_list = list(map(int, input().split()))
ans_list=[]
#답이 들어갈 list는 []으로 선언해서 공란으로 만들어줌

#num_list안에 있는 정수의 갯수를 세주는 함수
for i in range(len(num_list)):
    if num_list[i] < x :
        ans_list.append(num_list[i])
        #num_list 안에 있는 변수 i를 ans_list에 append 해주기

#list 안 값들이 str 형이면 변환해줄 필요가 없지만 int 형이라 변환 후
#join 함수를 써줘야 함

answer = " ".join([str(_) for _ in ans_list])
print(answer)