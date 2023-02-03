def solution(array):
    maximum = max(array)
    answer = [maximum, array.index(maximum)]
    return answer