def solution(s):
    answer = s.split(' ')
    new = s.split(' ')
    for n in range(1, len(new)):
        if new[n] == "Z":
            answer.remove(new[n-1])
            answer.remove(new[n])
    answer = list(map(int, answer))
    return sum(answer)