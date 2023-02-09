def solution(array):
    seven = [str(a) for a in array]
    answer = 0
    for s in seven:
        answer += s.count('7')
    return answer