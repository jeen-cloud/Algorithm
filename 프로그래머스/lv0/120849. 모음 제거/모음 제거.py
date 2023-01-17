def solution(my_string):
    english = 'aeiou'
    for t in english:
        my_string = my_string.replace(t, '')
        # print(t)
    return my_string