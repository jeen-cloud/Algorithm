def solution(num):
    answer = 0
    while answer <= 500:
        if num == 1:
            return answer
            break
        elif num % 2 == 0:
            num = num / 2
            answer += 1
            continue
        elif num % 2 == 1:
            num = (num * 3) + 1
            answer += 1
            continue
    return -1
