def solution(arr):
    answer = min(arr)
    arr.remove(answer)
    if arr == []:
        return [-1]
    return arr