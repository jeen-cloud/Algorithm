def solution(money):
    coffee = money // 5500
    trunc = money - (5500*coffee)
    answer = [coffee, trunc]
    return answer