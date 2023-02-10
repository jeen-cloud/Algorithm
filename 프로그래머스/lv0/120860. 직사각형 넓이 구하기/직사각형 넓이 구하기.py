def solution(dots):
    big = max(dots)
    small = min(dots)
    answer = (big[0] - small[0]) * (big[1]-small[1])
    return answer