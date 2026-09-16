def solution(n):
    answer = 0
    
    for i in range (1,n + 1):
        num = 0
        for j in range (1, i+1):
            if(num >= 2 and j != i):
                answer += 1
                break;
            elif (i % j == 0):
                num += 1
    
    return answer