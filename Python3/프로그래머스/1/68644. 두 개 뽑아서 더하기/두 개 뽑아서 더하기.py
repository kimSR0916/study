def solution(numbers):
    answer = []
    
    for i in range (len(numbers)):
        for j in range (i, len(numbers)):
            if (i != j):
                tmp = numbers[i] + numbers[j]
            
                if (tmp in answer):
                    pass
                else:
                    answer.append(tmp)


    answer.sort()
    return answer