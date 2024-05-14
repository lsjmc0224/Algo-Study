# 8진수 2진수 ( https://www.acmicpc.net/problem/1212 )
import sys

# 8진수 입력 받기
octal = sys.stdin.readline().strip()

# 8진수를 10진수로 변환한 후, 이를 다시 2진수로 변환
# int 함수의 두 번째 인자는 입력 값의 진법을 의미
binary = bin(int(octal, 8))[2:]  # bin 함수는 결과를 '0b' 접두사와 함께 반환하므로 [2:]로 접두사 제거

# 결과 출력
sys.stdout.write(binary)


'''
# input : 8진수 N

# input을 리스트형태로 쪼개서 받기 
import sys
input = sys.stdin.readline
N = list(map(int, input().rstrip()))

# 출력의 초기 세팅
output = ''

# 모든 경우의 수 표기
dic = {0 : '000',
       1 : '001',
       2 : '010',
       3 : '011',
       4 : '100',
       5 : '101',
       6 : '110',
       7 : '111'}

# 2진수로 바꾸기
for i in N:
    temp = i
    output += dic[i]

# 출력의 첫 수가 0이면 제외하고 출력
if output[0] == '0':
    print(output[1:])
else:
    print(output)
'''
