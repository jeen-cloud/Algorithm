def solution(angle):
    result = {'예각': 1, '직각':2, '둔각':3, '평각':4}
    if 0 < angle < 90:
        answer = '예각'
    elif angle == 90:
        answer = '직각'
    elif 90 < angle < 180:
        answer = '둔각'
    elif angle == 180:
        answer = '평각'
    return result[answer]