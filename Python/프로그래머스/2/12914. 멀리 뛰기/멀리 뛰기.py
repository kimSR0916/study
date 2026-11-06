import sys
sys.setrecursionlimit(2000)
#재귀리밋풀어주기

def solution(n):
    answer = 0
    memo = [0] * (n + 1)
    
    def dp_jump(num):
        if num <= 2:
            return num
        
        if memo[num] != 0:
            return memo[num]
        
        memo[num] = (dp_jump(num-1) + dp_jump(num-2)) % 1234567
        
        return memo[num]
    
    
    answer = dp_jump(n)
    return answer