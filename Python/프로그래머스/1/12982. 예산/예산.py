def solution(d, budget):
    answer = 0
    
    d.sort()

    count = 0
    i = 0

    while count < len(d) and i <= budget:
        if(i + d[count] == budget):
            count += 1
            break
        elif(i + d[count] < budget):
            i += d[count]
            count += 1
        else:
            break
    
    return count