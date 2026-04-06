def solution(s):
    answer = True
    
    try:
        tmp = int(s)
    except:
        answer = False
    
    if (len(s) != 4 and len(s) != 6):
        answer = False
    return answer