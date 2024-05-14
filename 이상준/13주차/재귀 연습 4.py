'''
문자열을 받아 문자 "x"가 들어간 첫 번째 인덱스를 반환하는 함수를 재귀적으로 작성하라.
'''
string = str(input())

def finding_x(string, i = 0):
    if string[i] == "x":
        return i
    else:
        return finding_x(string = string, i = i + 1)
    
print(finding_x(string))