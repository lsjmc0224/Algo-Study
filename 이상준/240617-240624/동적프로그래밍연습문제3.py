'''
다음은 11장 연습무넺에 니왔던 "유일 경로" 문제의 해법이다. 메모이제이션으로 표율성을 개선하자.
def unique_paths(rows, columns):
    return 1 if rows==1 || columns == 1
    return unique_paths(rows-1, columns) + unique_paths(rows, columns - 1)
end
'''
def unique_paths(rows, columns):
    ret = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j == 0:
                ret[i][j] = 1
            else:
                ret[i][j] = ret[i-1][j] + ret[i][j-1]
    return ret[rows-1][columns-1]
print(unique_paths(3, 5))

'''
문제점 1: 잘못된 초기화
리스트를 초기화할 때 [[0] * columns] * rows를 사용하면 각 행이 동일한 리스트 객체를 참조하게 됩니다. 따라서 하나의 값을 변경하면 모든 행이 변경됩니다.
'''