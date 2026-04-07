def solution(s):
    answer = []
    
    c = 0
    i = 0

    while s != '1':
        c += s.count('0')
        i += 1
        s = s.replace('0', '')
        s = format(len(s), 'b')
    
    answer.append(i)
    answer.append(c)
    
    return answer