def solution(num, k):
    number = str(num)
    if str(k) in number:
        return number.index(str(k))+1
    else:
        return -1