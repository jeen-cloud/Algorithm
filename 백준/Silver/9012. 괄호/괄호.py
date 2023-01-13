a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sumed = 0
    for t in s:
        if t == '(' :
            sumed += 1
        elif t == ')':
            sumed -= 1
            if sumed < 0:
                print('NO')
                break
    if sumed == 0:
        print('YES')
    elif sumed > 0:
        print('NO')
