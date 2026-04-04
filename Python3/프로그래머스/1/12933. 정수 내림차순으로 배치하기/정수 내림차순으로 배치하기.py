def solution(n):
    answer = 0
    
    nums = []

    while n > 0:
        nums.append(n % 10)
        n = n // 10
    
    nums.sort(reverse = True)
    answer = int("".join(map(str,nums)))
    
    return answer