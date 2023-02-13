def solution(polynomial):
    poly = polynomial.split(' + ')
    ans = 0
    num = 0
    for a in poly:
        if 'x' in a:
            if a == 'x':
                ans += 1
            else:
                a = a.replace('x', '')
                ans += int(a)
        elif a.isdigit() == True:
            num += int(a)
    if ans == 1:
        ans = ''
    if ans !=0 and num != 0:
        return f'{ans}x + {num}'
    elif num == 0:
        return f'{ans}x'
    elif ans == 0 :
        return f'{num}'