def solution(n):
    a = n ** 0.5
    if (a - int(a)) == 0 :
        return (a + 1) ** 2
    else:
        return -1