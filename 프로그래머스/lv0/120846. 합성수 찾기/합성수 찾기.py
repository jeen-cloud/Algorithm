def solution(n):
    prime = []
    for i in range(3, n+1):
        for j in range(2, i):
            if i % j == 0:
                pass 
            elif i % j != 0:
                prime.append(i)
        
    answer = 0
    return prime