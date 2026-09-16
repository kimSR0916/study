def solution(n, m):
    answer = []
    
    big = max(n,m)

    for i in range (1, big + 1):
        if (n % i == 0 and m % i == 0):
            result = i
        
    div_n = n // result
    div_m = m // result

    if div_m == 0:
        res = result * div_n
    elif div_n == 0:
        res = result * div_m
    else:
        res = result * div_n * div_m
    
    answer.append(result)
    answer.append(res)

    return answer