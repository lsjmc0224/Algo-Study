'''
삼각수라는 수열이 있다. 1, 3, 6, 10, 15, 21로 시작해 패턴 내 N번째 수까지 일정 패턴이 이어진다. 
N번째 값은 N에 바로 앞 숫자를 더한 값이다.
N이 주어지면 N번째 삼각수를 찾는 함수를 재귀적으로 작성하라
'''

# input : N
N = int(input())

# 삼각수 재귀함수
def triangle(N):
    if N <= 1:
        return 1
    else:
        return N + triangle(N = N-1)
print(triangle(N))