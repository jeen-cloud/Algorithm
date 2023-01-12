def solution(hp):
    gen = hp // 5
    sol = (hp%5) // 3
    work = (hp%5)%3
    return gen+sol+work