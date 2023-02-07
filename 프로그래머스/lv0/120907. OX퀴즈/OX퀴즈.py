def solution(quiz):
    answer = []
    for q in quiz:
        k = q.split('=')
        if eval(k[0]) == eval(k[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer