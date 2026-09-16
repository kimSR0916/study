def solution(a, b):
    answer = 0
    
    if a > b:
        ma = a
        mi = b
    else:
        ma = b
        mi = a
    for i in range (mi,ma + 1):
        answer += i
        
    return answer