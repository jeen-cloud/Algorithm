def solution(n):
    number = list(''.join(str(n)))
    answer = [int(i) for i in number]
    return sum(answer)