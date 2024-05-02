# 2×n 타일링 2 ( https://www.acmicpc.net/problem/11727 )
'''
input : 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
output : 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지.
'''
n = int(input())
one_by_two = [0] + [1] + [0]*999
two_by_one = [0]*1001
two_by_two = [0]*1001


for i in range(2, n+1):
    one_by_two[i] = one_by_two[i-1] + two_by_one[i-1] + two_by_two[i-1]
    two_by_one[i] = one_by_two[i-1]
    two_by_two[i] = one_by_two[i-1]

output = one_by_two[n] + two_by_one[n] + two_by_two[n]
print(output%10007)