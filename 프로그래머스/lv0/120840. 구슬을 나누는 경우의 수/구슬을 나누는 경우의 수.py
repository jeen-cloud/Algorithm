def solution(balls, share):
    b = 1
    h = 1
    n = 1
    for s in range(1, balls+1):
        b *= s
    for i in range(1, share+1):
        h *= i
    answ = balls-share    
    for a in range(1, answ+1):
        n *= a
    answer = int(b/(h*n))
    return answer