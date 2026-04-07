def solution(t, p):
    answer = 0
    l = len(p)
    
    for i in range (len(t) - l + 1):
        res = ''
        for j in range (i, i + l):
            res += t[j]
        
        if int(p) >= int(res):
            answer += 1
    return answer