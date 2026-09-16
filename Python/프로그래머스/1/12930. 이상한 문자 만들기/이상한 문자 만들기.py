def solution(s):
    answer = ''
    n = 0
    
    for i in s:
        if i != ' ':
            if(n % 2 == 0):
                answer = answer + i.upper()
            else:
                answer = answer + i.lower()
            n += 1
        else:
            answer += i
            n = 0
        
    return answer