def solution(array):
    arr_dict = {}
    for i in array:
        arr_dict[i] = 0
    for i in array :
        arr_dict[i] += 1
    arr= sorted(arr_dict, key=arr_dict.get)
    if len(arr) == 1:
        return arr[-1]
    else: 
        if arr_dict.get(arr[-1]) == arr_dict.get(arr[-2]):
            return -1
        else:
            return arr[-1]

# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1
        
