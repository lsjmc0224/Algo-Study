# input D, K
D, K = map(int, input().split())

def find_tteok_count(D, K):
    fib = [0] * (D + 1)
    fib[1] = 1
    fib[2] = 1

    for i in range(3, D + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    for A in range(1, K // fib[D - 1] + 1):
        if (K - A * fib[D - 2]) % fib[D - 1] == 0:
            B = (K - A * fib[D - 2]) // fib[D - 1]
            return A, B

A, B = find_tteok_count(D, K)
print(A)
print(B)