def solution(array):
    array = sorted(array)
    median = len(array)//2
    answer = array[median]
    return answer