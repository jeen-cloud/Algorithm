def solution(numbers, k):
    answer = numbers*((k*2//len(numbers))+1)
    return answer[2*k-2]