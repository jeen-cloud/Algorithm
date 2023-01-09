def solution(n, k):
    if n < 10:
        answer = (12000*n) + (2000*k)
    elif n >= 10:
        ans = n // 10
        answer = (12000*n) + (2000*(k-ans))
    return answer