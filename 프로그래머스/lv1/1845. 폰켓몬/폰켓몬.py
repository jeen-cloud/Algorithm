def solution(nums):
    dict1 = {}
    for i in nums:
        dict1[i] = 0
    for n in nums:
        dict1[n] += 1
    if len(dict1.keys()) <= len(nums)/2:
        return len(dict1.keys())
    else:
        return len(nums)/2