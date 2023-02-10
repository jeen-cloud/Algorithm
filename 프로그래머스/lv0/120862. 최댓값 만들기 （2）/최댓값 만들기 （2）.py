def solution(numbers):
    numbers = sorted(numbers)
    minus = list(filter(lambda x:x<0, numbers))
    ans = 0
    answer = numbers[-1] * numbers[-2]
    if len(minus) > 1:
        ans = numbers[0] * numbers[1]
        if ans > answer:
            return ans
        else:
            return answer
    else:
        return answer