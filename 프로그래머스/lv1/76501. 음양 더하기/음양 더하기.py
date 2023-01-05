def solution(absolutes, signs):
    li1 = []
    for a, b in zip(signs, absolutes):
        if a == True:
            li1.append(b)
        else:
            li1.append(-b)
    answer = sum(li1)
    return answer