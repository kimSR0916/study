def solution(k, tangerine):
    answer = 0
    
    counts = {}
    for x in tangerine:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    result = dict(sorted(counts.items(), key = lambda x : x[1], reverse = True))
    
    res = 0
    for i in result.values():
        res += i
        answer += 1
        
        if res >= k:
            break
        
    
    return answer