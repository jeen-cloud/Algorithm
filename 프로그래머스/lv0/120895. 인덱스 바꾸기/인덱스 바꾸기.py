def solution(my_string, num1, num2):
    string = list(''.join(my_string))
    str2 = string[num2]
    string[num2] = string[num1]
    string[num1] = str2
    string = ''.join(string)
    return string