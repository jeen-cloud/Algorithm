def solution(d, budget):
    answer = []
    for i in sorted(d):
        answer.append(i)
        if sum(answer) > budget:
            return len(answer)-1
    if sum(d) <= budget:
        return len(d)