def solution(sides):
    maximum = list(range(max(sides) - min(sides)+1, max(sides)+1))
    maxi = list(range(max(sides)+1, min(sides) + max(sides)))
    answer = list(set(maximum + maxi))
    return len(answer)