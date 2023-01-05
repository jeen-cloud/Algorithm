def solution(s):
    if len(s) % 2 == 0 :
        a = len(s)/2
        return s[int(a-1):int(a+1)]
    if len(s) % 2 == 1 :
        a = len(s)//2
        return s[int(a)]