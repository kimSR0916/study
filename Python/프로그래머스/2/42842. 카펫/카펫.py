def solution(brown, yellow):
    answer = []
    
    i = 1
    j = 1
    
    area = brown + yellow
    total = (brown + 4) // 2
    
    while i < 5000:
        if (i * j == area):
            if(i + j == total):
                answer.append(max(i,j))
                answer.append(min(i,j))
                break
            else:
                j = 0
                i += 1
        elif (i * j > area):
            j = 0
            i += 1
                
        j += 1
    return answer