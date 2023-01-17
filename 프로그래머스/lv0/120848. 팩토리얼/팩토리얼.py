def solution(n):
    f = 0
    while f <= 10:
        f += 1
        factorial = 1
        for i in range(1, f+1) :
            factorial *= i
        if factorial > n:
            return f-1
        elif factorial == n:
            return f