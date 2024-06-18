'''
다음 함수를 메모이제이션을 이용해 최적화하자.

def golomb(n):
    return 1 if n == 1
    return 1 + golomb(n - golomb(golomb(n-1)))
'''
import sys
input = sys.stdin.readline
n = int(input())
def golomb(n):
    ret = [0] + [1] + [0] * (n - 1)
    for i in range(2, n + 1):
        ret[i] = 1 + ret[i - ret[ret[i-1]]]
    print(ret)

golomb(n)