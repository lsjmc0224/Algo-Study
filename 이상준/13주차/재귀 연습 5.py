'''
유일경로라고 불리는 문제가 있다. 행과 열로 이뤄진 격자판이 있다고 하자.
행 수와 열 수를 받아 왼쪽 맨 윗칸에서 오른쪽 맨 아랫칸카지 가는 최단 경로의 개수를 계산하는 함수를 작성하라
'''
Y, X = map(int, input().split())

def finding_route(Y, X):
    if X <= 1 or Y <= 1:
        return 1
    else:
        return finding_route(X-1, Y) + finding_route(X, Y-1)
    
print(finding_route(Y, X))