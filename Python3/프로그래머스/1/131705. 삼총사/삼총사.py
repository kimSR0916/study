def solution(number):
    answer = 0
    
    for i in  range (len(number) - 2):
        for j in range(i, len(number) - 1):
            for k in range(j, len(number)):
                res = number[i] + number[j] + number[k]
                if i != j and i != k and k != j:
                    if res == 0:
                        answer += 1
    
    return answer