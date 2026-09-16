def solution(n):
    answer = 0
    
    tmp = format(n, 'b')
    c = tmp.count('1')

    while 1:
        n += 1
        tmp = format(n, 'b')
    
        if c == tmp.count('1'):
            answer = n
            break
    
    return answer