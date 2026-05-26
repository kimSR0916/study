def solution(a, b, n):
    answer = 0
    i = 0
    bottle = n
    while n >= a:
        while i <= n:
            tmp = i * a
            if tmp > n:
                bottle = (i - 1) * b
                answer += bottle
                i = 0
                n = n - tmp + a + bottle
            elif n < a:
                break
            else:
                i += 1
    
    return answer