def solution(participant, completion):
    dict1 = {}
    for p in participant:
        dict1[p] = 0
    for p in participant:
        dict1[p] += 1
    for c in completion:
        dict1[c] -= 1
    
    for k in dict1.keys():
        if dict1.get(k) == 1 :
            return k
    
