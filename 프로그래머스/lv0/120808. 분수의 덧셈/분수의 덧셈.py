import math
def solution(denum1, num1, denum2, num2):
    gcd1 = math.gcd(num1, num2)
    num3 = int((num1*num2) / gcd1)
    denum3 = int((denum1*(num2) + denum2*(num1)) / gcd1)
    answer = [denum3, num3]
    gcd2 = math.gcd(denum3, num3)
    if gcd2 == 1 :
        answer = [denum3, num3]
    else:
        answer = [denum3/gcd2, num3/gcd2]
    return answer