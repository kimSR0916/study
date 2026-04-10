def solution(sizes):
    answer = 0
    
    tmp1 = 0
    tmp2 = 0

    for i in range(len(sizes)):
        sizes[i].sort()
    
        if tmp1 < sizes[i][0]:
            tmp1 = sizes[i][0]
        if tmp2 < sizes[i][1]:
            tmp2 = sizes[i][1]
        
    answer = tmp1 * tmp2
    
    return answer