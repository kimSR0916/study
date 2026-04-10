def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        j = i
        tmp = 0
        while tmp < n:
            tmp += j
            j += 1
        
            if tmp == n:
                answer += 1
    
    return answer