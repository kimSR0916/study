def solution(s):
    answer = []
    list_s = []
    
    for i in range (len(s)):
        if list_s == []:
            list_s.append(s[i])
            answer.append(-1)
        elif s[i] in list_s:
            answer.append(i - list_s.index(s[i]))
            list_s[list_s.index(s[i])] = ''
            list_s.append(s[i])
        else:
            list_s.append(s[i])
            answer.append(-1)
        
        
    return answer