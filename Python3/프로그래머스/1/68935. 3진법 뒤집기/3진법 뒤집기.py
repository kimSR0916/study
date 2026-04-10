def solution(n):
    answer = 0
    res = ''

    while n > 0:
        res = str(n % 3) + res
        n = n//3
    
    for i in range (len(res)):
        if i == 0:
            answer += 1 * int(res[i])
        else:
            tmp = 1
            for j in range(i):
                tmp = tmp * 3
            answer += tmp * int(res[i])
        
    return answer