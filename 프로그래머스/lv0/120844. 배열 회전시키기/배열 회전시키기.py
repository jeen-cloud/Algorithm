def solution(numbers, direction):
    if direction == 'right':
        right = numbers[-1]
        numbers.insert(0, right)
        numbers.pop()
    else:
        left = numbers[0]
        numbers.pop(0)
        numbers.append(left)
    return numbers