def solution(array, height):
    answer = list(filter(lambda a : a>height, array))
    return len(answer)