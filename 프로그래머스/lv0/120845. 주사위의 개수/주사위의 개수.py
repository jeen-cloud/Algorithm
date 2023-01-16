def solution(box, n):
    one = (box[0] // n ) * (box[1] // n)
    answer = box[2] // n * one
    return answer