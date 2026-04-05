def solution(arr, divisor):
    answer = []
    
    n = 0

    for i in range(len(arr)):
        if(arr[i] % divisor == 0):
            answer.append(arr[i])
            n += 1
        
    if n == 0:
        answer.append(-1)
        
    answer.sort()
    
    return answer