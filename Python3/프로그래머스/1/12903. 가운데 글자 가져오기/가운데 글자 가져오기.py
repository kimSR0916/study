def solution(s):
    answer = ''
    
    l = len(s)
    n = l // 2

    if l % 2 == 0:
        answer = s[n - 1] + s[n]
    else:
        answer = s[n]
    
    
    return answer