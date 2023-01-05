def solution(num_list):
    answer = []
    while 1:
        if num_list == []:
            break
        i = num_list.pop()
        answer.append(i)
    return answer