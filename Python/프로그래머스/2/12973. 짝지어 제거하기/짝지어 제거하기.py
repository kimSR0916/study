def solution(s):
    answer = 1
    list_s = []
    
    for i in s:
        if list_s == []:
            list_s.append(i)
        elif list_s[-1] == i:
            list_s.pop()
        else:
            list_s.append(i)
            
    if list_s != []:
        answer = 0
        
    return answer