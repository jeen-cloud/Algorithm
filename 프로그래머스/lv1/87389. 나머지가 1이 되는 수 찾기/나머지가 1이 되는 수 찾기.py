def solution(n):
    answer = min([num for num in range(1, n+1) if n % num == 1])
    return answer