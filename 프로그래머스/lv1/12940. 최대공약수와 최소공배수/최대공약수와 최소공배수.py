def solution(n, m):
    j = set([i for i in range(1, n + 1) if n % i == 0])
    k = set([i for i in range(1, m + 1) if m % i == 0])
    a = max(j&k)
    b = (m*n)/a
    return [a, b]