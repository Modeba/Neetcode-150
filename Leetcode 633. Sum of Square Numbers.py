from math import sqrt, ceil, floor

def judgeSquareSum(c):
    if c <= 2:
        return True
    
    for i in range(c):
        for e in range(i, c):
            print(i, e)
            curr = i ** 2 + e ** 2
            if curr == c:
                return True
    return False

def judgeSquareSumFast(c):
    if c <= 2:
        return True
    
    root = ceil(sqrt(c))
    for i in range(root + 1):
        second = c - i ** 2
        if second < 0:
            break
        second = sqrt(second)
        if second == int(second):
            return i, i ** 2, second, second ** 2
    return False

print(judgeSquareSumFast(549))