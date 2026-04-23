def solution(s, n):
    answer = ''
    
    for i in s:
        if i.isalpha():
            tmp = ord(i)
        
            if (tmp + n) > ord('z') and i.islower():
                answer += chr(tmp + n - 26)
            elif (tmp + n) > ord('Z') and i.isupper():
                answer += chr(tmp + n - 26)
            else:
                answer += chr(tmp + n)
        else:
            answer += i
    
    return answer