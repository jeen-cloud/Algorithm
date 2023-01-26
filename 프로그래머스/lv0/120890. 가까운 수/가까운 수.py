def solution(array, n):
    ans = [abs(n-a) for a in sorted(array)]
    answer = ans.index(min(ans))
    return sorted(array)[answer]