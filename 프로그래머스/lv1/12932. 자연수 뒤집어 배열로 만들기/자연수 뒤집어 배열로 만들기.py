def solution(n):
    answer = list(''.join(str(n)))
    answer.reverse()
    return  [int(i) for i in answer]