def solution(n):
    answer = fibonacci(n)
    return answer % 1234567

def fibonacci(n):
    tmp = []
    for i in range (n + 1):
        if i == 0:
            tmp.append(0)
        elif i == 1:
            tmp.append(1)
        else:
            tmp.append(tmp[i - 1] + tmp[i - 2])
    
    return tmp[n]