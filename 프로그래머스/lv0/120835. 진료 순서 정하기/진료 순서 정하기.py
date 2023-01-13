def solution(emergency):
    emer = sorted(emergency, reverse=True)
    leng = range(1, len(emergency)+1)
    emer_dict = dict(zip(emer, leng))
    answer = [emer_dict[e] for e in emergency]
    return answer