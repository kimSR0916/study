def solution(s):
    answer = 0
    
    try:
        answer = int(s)
    except:
        s.lstrip()
        answer = int(s)
        
    return answer