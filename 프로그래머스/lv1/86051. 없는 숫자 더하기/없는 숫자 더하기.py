def solution(numbers):
    num = list(range(10))
    answer  =  sum(set(num) - set(numbers))
    return answer