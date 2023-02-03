def solution(my_string):
    number = my_string.split(' ')
    answer = int(number[0])
    for s in range(len(number)):
        if number[s] == '+':
            answer += int(number[s+1])
        elif number[s] == '-':
            answer -= int(number[s+1])
    return answer