def solution(left, right):
    answer = []
    number = list(range(left, right+1))
    for n in number:
        if (n ** 0.5) == int(n**0.5):
            number.remove(n)
            answer.append(n)
    return sum(number) - sum(answer)