def solution(x):
    answer = True
    
    n = x
    num = 0
    while n > 0:
        num += n % 10
        n = n // 10
    
    if (x % num != 0):
        answer = False
    return answer