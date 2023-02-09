def solution(my_str, n):
    answer = [my_str[s:s+n] for s in range(0, len(my_str), n)]
    return answer