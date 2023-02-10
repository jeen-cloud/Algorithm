def solution(keyinput, board):
    key = {'left':[-1,0], 'right':[1,0], 'up':[0,1], 'down':[0,-1]}
    ans = [key[k] for k in keyinput]
    answer = [0, 0]
    for a in ans:
        for s in range(len(a)):
            if abs(answer[s]) <= (board[s] // 2): 
                answer[s] += a[s]
                if abs(answer[s]) > (board[s] // 2):
                    answer[s] -= a[s]
            else:
                pass
    return answer