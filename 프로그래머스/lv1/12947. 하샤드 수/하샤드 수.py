def solution(x):
    answer = []
    for a in range(len(str(x))):
        answer.append(int(str(x)[a]))
    if x % sum(answer) == 0:
        return True
    return False