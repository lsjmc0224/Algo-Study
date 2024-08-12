while True :
    try : 
        print(input())
    except EOFError: #EndOfFile! 더이상 입력값이 안 들어올 때
        break;