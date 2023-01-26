def solution(s):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    answer = sorted([k for k, v in dic.items() if v == 1])
    return ''.join(answer)