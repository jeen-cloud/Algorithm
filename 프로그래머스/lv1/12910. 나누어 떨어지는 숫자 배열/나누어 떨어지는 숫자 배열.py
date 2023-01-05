def solution(arr, divisor):
    answer = sorted(list(filter(lambda a : a%divisor==0, arr)))
    if answer == []:
        return [-1]
    else: return answer