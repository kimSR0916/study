def solution(s):
    answer = True
    
    result = 0
    
    for w in s:
        if result == -1:
            answer = False
        if w == '(':
            result += 1
        else:
            result -= 1
            
    if result != 0:
        answer = False
        
    return answer