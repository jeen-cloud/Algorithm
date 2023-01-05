def solution(num_list):
    a = [i for i in num_list if i%2 == 0]
    b = [i for i in num_list if i%2 == 1]
    answer = [len(a), len(b)]
    return answer